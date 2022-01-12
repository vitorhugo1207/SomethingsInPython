query = '''
query ($id: Int, $page: Int, $perPage: Int, $search: String) {
  Page(page: $page, perPage: $perPage) {
    media(id: $id, search: $search, type: ANIME) {
      id
      title {
        romaji
        english
        native
      }
      episodes
      description
      format
      status
      duration
      genres
      tags {
        name
      }
      studios {
        nodes {
          name
        }
      }
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      season
      seasonYear
      seasonInt
      countryOfOrigin
      coverImage {
        medium
        large
        extraLarge
      }
      bannerImage
      source
      hashtag
      synonyms
      meanScore
      averageScore
      nextAiringEpisode {
        timeUntilAiring
        airingAt
      }
      trailer {
        id
        thumbnail
        site
      }
      staff(sort: FAVOURITES_DESC) {
        edges {
          node {
            name {
              full
            }
            id
          }
        }
      }
      characters(role: MAIN) {
        edges {
          node {
            name {
              full
            }
          }
        }
      }
    }
  }
}
'''
