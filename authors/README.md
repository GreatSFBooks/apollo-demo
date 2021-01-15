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