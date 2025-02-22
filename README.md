# reptile_shipper
A tool used to make sure that various routing cities have weather fit for reptilian friends

# Reptile Shipper API
Local and production currently use the same Geopy account. There's a limit of 1000 requests a day. In the future it might make sense to separately rate limit local/prod. For now, 
since it's just me toiling away here, I'm tracking the rate limiting for both in the same place. Because I don't want a random Geopy bill.

## Authentication
Since all requests are coming from **my** app, there is a token stored on the enviornments to authorize requests.
## Local Development
To run the Reptile shipper API locally, use the following gunicorn command: gunicorn -w 1 -b 0.0.0.0:10000 app:app (increase number of workers if needed)

## Production Deployment
### Render
The production API is run on a service called Render. Currently on the FREE tier. 

Since we're using the free tier, the api is spun down after not being used for a while. This can be changed with like a $7/month plan

### Production Flask Server
The local debugging can be done with python3 app.py or by running gunicorn. For production we MUST use gunicorn.

The default PORT for render is 10000 (https://render.com/docs/web-services?_gl=1*1gl75n*_ga*NzY1MTM5NTUyLjE3NDAxODQ4OTA.*_ga_QK9L9QJC5N*MTc0MDE4NDg4OS4xLjEuMTc0MDE4NDk0MS44LjAuMA..#port-binding) - so we use that for the gunicorn command to run the production service.

