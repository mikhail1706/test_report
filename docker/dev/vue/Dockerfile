FROM node:10.19.0
WORKDIR /app
COPY ./report_test_project_ui/package*.json ./
RUN npm install
COPY ./report_test_project_ui .
#EXPOSE 8080
#CMD ["npm", "run", "serve"]