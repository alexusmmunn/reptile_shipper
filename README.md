# reptile_shipper
A tool used to make sure that various routing cities have weather fit for reptilian friends

## Production Deployment

**Frontend and backend deployment are done automatically when changes are pushed to main.**

Production: https://reptile-shipper.vercel.app/ 

The frontend is currently run on Vercel (https://vercel.com/guides/deploying-react-with-vercel). **Manual deployment required**

## Reptile Shipper App (Frontend)
Run locally with NPM start. Frontend env vars are set up to ping the local backend when frontend is running locally.

## Reptile Shipper API (Backend)
A wrapper around the open-mateo API https://open-meteo.com/ 

### Authentication
Since all requests are coming from **my** app, there is a token stored on the enviornments to authorize requests.
### Local Development
To run the Reptile shipper API locally, use the following gunicorn command: gunicorn -w 1 -b 0.0.0.0:10000 app:app (increase number of workers if needed)

### Production Deployment
#### Render
The production API is run on a service called Render. Currently on the FREE tier. 

Since we're using the free tier, the api is spun down after not being used for a while. This can be changed with like a $7/month plan

#### Production Flask Server
The local debugging can be done with python3 app.py or by running gunicorn. For production we MUST use gunicorn.

The default PORT for render is 10000 (https://render.com/docs/web-services?_gl=1*1gl75n*_ga*NzY1MTM5NTUyLjE3NDAxODQ4OTA.*_ga_QK9L9QJC5N*MTc0MDE4NDg4OS4xLjEuMTc0MDE4NDk0MS44LjAuMA..#port-binding) - so we use that for the gunicorn command to run the production service.

