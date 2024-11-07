FROM emscripten/emsdk:3.1.36 as build
run emsdk install 2.0.7
run emsdk activate 2.0.7
run bash -c "source /emsdk/emsdk_env.sh"
ADD code code
ADD dist dist
ADD screenshots screenshots
ADD server server
run cd code && make

from  python:3.10.15-slim-bookworm
COPY --from=build /src/dist ./
RUN python3 -m pip install flask
RUN python3 -m pip install gunicorn

ADD app.py .
EXPOSE 8080
CMD gunicorn --bind :8080 app:app