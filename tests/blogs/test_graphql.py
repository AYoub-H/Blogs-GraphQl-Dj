import pytest
from tests.blogs.factories import UserFactory, BlogFactory


@pytest.mark.django_db
def test_queries(authenticated_graphql_client):
    query = """
{
  blogs {
    id
    title
    author {
      id
      lastName
      phoneNumber
    }
  }
}
    """
    user = UserFactory()
    blog = BlogFactory()
    result = authenticated_graphql_client.execute(query)
    assert len(result["data"]["blogs"]) == 1
    assert eval(result["data"]["blogs"][0]["id"]) == blog.id

    # get specific user
    # query = """
    # query user($id: ID!){
    #     user(id: $id) {
    #         lastName
    #     }
    # }
    # """
    # result = authenticated_graphql_client.execute(query, variable_values={"id": user.id})
    # assert result == {
    #     "data": {"degree": {"name": user.last_name,}}
    # }
