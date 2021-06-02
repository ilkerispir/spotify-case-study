# Spotify Case Study

## Run Command

```bash
cd backend; dev_appserver.py app.yaml
```

## Backend

* Lang: [Python 2.7](https://www.python.org/)
* Framework: [webapp2](https://webapp2.readthedocs.io/en/latest/)

## Frontend

* Lang: [Node v16](https://nodejs.org/en/)
* UI: [React.js](https://reactjs.org/)
* UI Kit: [Antd](https://ant.design/)
* Modules: [Axios](https://www.npmjs.com/package/axios)


## React.js Error Watch Problem
```bash
fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```