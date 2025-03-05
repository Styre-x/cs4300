Hello!

Very easy to run, python3 manage.py runserver 0.0.0.0:3000

API:
Returns JSON with IDs for the booking/seat/movie. 


To add: send a post reqest with the json as required:

BOOKINGS:
`
{
    "movie": null,
    "seat": null,
    "user": null
}
`

MOVIES:`{
    "title": "",
    "description": "",
    "release_date": null,
    "duration": null
}`

SEATS:
`{
    "seat_number": "",
    "is_booked": false
}`

To delete: send a delete request to the endpoint followed by the ID to delete: /api/movies/1/

To Update:

Send a PUT/PATCH request with the updated JSON header: /api/movies/1/