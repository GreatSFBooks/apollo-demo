package graph

// This file will be automatically regenerated based on the schema, any resolver implementations
// will be copied through when generating and any unknown code will be moved to the end.

import (
	"context"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"

	"github.com/jesse-apollo/apollo-demo/authors/graph/generated"
	"github.com/jesse-apollo/apollo-demo/authors/graph/model"
)

func (r *entityResolver) FindAuthorByName(ctx context.Context, name string) (*model.Author, error) {
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

	for _, author := range authors {
		if (*author).Name == name {
			return author, nil
		}
	}

	return nil, fmt.Errorf("Author not found.")
}

// Entity returns generated.EntityResolver implementation.
func (r *Resolver) Entity() generated.EntityResolver { return &entityResolver{r} }

type entityResolver struct{ *Resolver }
