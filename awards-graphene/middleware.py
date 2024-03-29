import time
from datetime import datetime
from functools import partial

class TracingMiddleware(object):
    DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

    def __init__(self):
        #print("init")
        self.resolver_stats = list()
        self.reset()

    def reset(self):
        #print("reset")
        self.start_time = self.now()
        self.end_time = None
        self.parsing_start_time = None
        self.parsing_end_time = None
        self.validation_start_time = None
        self.validation_end_time = None

    def start(self):
        #print("start")
        self.reset()
        self.start_time = self.now()

    def end(self):
        self.end_time = self.now()

    def parsing_start(self):
        #print("parsing st")
        self.parsing_start_time = self.now()

    def parsing_end(self):
        self.parsing_end_time = self.now()

    def validation_start(self):
        #print("val st")
        self.validation_start_time = self.now()

    def validation_end(self):
        self.validation_end_time = self.now()

    def now(self):
        #if PY37:
        return time.time_ns()

        #return int(time.time() * 1000000000)

    @property
    def start_time_str(self):
        start_time_seconds = float(self.start_time / 1000000000)
        return datetime.fromtimestamp(start_time_seconds).strftime(self.DATETIME_FORMAT)

    @property
    def end_time_str(self):
        end_time_seconds = float(self.end_time / 1000000000)
        return datetime.fromtimestamp(end_time_seconds).strftime(self.DATETIME_FORMAT)

    @property
    def duration(self):
        if not self.end_time:
            raise ValueError("Tracing has not ended yet!")

        return self.end_time - self.start_time

    def get_tracing_extension_dict(self):
        result = dict(
            version=1,
            startTime=self.start_time_str,
            endTime=self.end_time_str,
            duration=self.duration,
            parsing=dict(
                startOffset=self.parsing_start_time - self.start_time,
                duration=self.parsing_end_time - self.parsing_start_time,
            ),
            execution=dict(resolvers=self.resolver_stats),
        )

        if self.validation_start_time and self.validation_end_time:
            result["validation"] = dict(
                startOffset=self.validation_start_time - self.start_time,
                duration=self.validation_end_time - self.validation_start_time,
            )

        return result

    def _after_resolve(self, start_time, resolver_stats, info, data):
            end = time.time()
            #print("1")
            elapsed_ms = (end - start_time) * 1000
            #print("2")
            #print(self.start_time)
            stat = {
                "path": info.path,
                "parentType": str(info.parent_type),
                "fieldName": info.field_name,
                "returnType": str(info.return_type),
                "startOffset": self.now() - self.start_time,
                "duration": elapsed_ms,
            }
            #print("3")
            resolver_stats.append(stat)
            #print("4")
            self.reset()
            return data

    def resolve(self, _next, root, info, *args, **kwargs):
        self.start()
        start = time.time()
        on_result_f = partial(self._after_resolve, start, self.resolver_stats, info)
        return _next(root, info, *args, **kwargs) \
            .then(on_result_f)