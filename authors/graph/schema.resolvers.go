package graph

// This file will be automatically regenerated based on the schema, any resolver implementations
// will be copied through when generating and any unknown code will be moved to the end.

import (
	"context"
	"encoding/json"
	"io/ioutil"
	"os"

	"github.com/mentat/apollo-demo/graph/generated"
	"github.com/mentat/apollo-demo/graph/model"
)

func (r *queryResolver) Authors(ctx context.Context) ([]*model.Author, error) {
	var authors []*model.Author

	jsonFile, err := os.Open("authors.json")
	// if we os.Open returns an error then handle it
	if err != nil {
		return nil, err
	}

	// defer the closing of our jsonFile so that we can parse it later on
	defer jsonFile.Close()

	byteValue, _ := ioutil.ReadAll(jsonFile)

	err = json.Unmarshal(byteValue, &authors)

	if err != nil {
		return nil, err
	}

	return authors, nil
}

// Query returns generated.QueryResolver implementation.
func (r *Resolver) Query() generated.QueryResolver { return &queryResolver{r} }

type queryResolver struct{ *Resolver }
