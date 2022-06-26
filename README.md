# bombardier-api
This is an application that exposes an endpoint to query Aircraft data and filter it by model, weight class and tags.

## Usage
The endpoint is reachable at: http://159.203.36.66:7007/api/aircraft/
The filters are named ˋmodelˋ, ˋatct_weight_classˋ and ˋtagˋ. They are usable as query parameters like the following;
http://159.203.36.66:7007/api/aircraft/?model=Cougar&atct_weight_class=Small%20Eqpt&tag=commercial

## Notes and asumptions
  - all the aircraft parameters are saved as string for the exercise purpose
  - the csv headers have been cleaned up and imported
  - the tag filter can accept a single tag or a comma separated list and will look for any instance that contains one or more of the specified tags. Example: http://159.203.36.66:7007/api/aircraft/?tag=single,commercial

## Local installation
pre-requisite: Docker and docker-compose
The application can be installed locally using Docker by running ˋdocker-compose upˋ from the project root directory.
After the containers are created, the endpoint should be available  at ˋhttp://localhost:7007/api/aircraft/ˋ

## Contributions and improvement
This application is developed using the Django Framework. There is a single django application named aircraft containing the necessary model, view and serializer. The Database used for this purpose is sqlite3

Improvements:
 - upgrade from sqlite to Postgres
 - Update the models to use the correct data types and re-import the data
 - use a better tag format (i.e by using many to many keys linking to a separate model)
 - use predefined value list for limited parameters like the wing tip configuration
