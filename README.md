# Docker Compose

1. Buat Direktori Project. misal DockerCompose
2. Lalu Buat directori baru didalamnya dengan nama biodata
3. pada directori buat 3 buah file yaitu

	a. Dockerfile
		```
		FROM python:3-onbuild
		COPY . /usr/src/app
		CMD ["python", "api.py"]
		```
		
	b. api.py
		```
		# Product Service
		# Import framework
		from flask import Flask
		from flask_restful import Resource, Api
		# Instantiate the app
		app = Flask(__name__)
		api = Api(app)
		class Biodata(Resource):
    		def get(self):
        		return {
            		'bio': ['Yudha Pratama Putra', '155410053', 'Teknik Informatika']
        		}
		# Create routes
		api.add_resource(Biodata, '/')
		# Run the application
		if __name__ == '__main__':
		    app.run(host='0.0.0.0', port=80, debug=True)
		```
		
	c. requirement.txt
		```
		Flask==0.12
		flask-restful==0.3.5
		```
4. lalu buat direktori website untuk menyimpan file index.php
	```
	<html>
    	<head>
        	<title>DockerCompose</title>
    	</head>
    	<body>
        	<h1>Hello World :3</h1>
        	<ul>
            	<?php
            	$json = file_get_contents('http://biodata-service/');
            	$obj = json_decode($json);
            	$biodata = $obj->bio;
            	foreach ($biodata as $bio) {
                	echo "$bio<br>";
            	}
            	?>
        	</ul>
    	</body>
	</html>
	```
5. lalu terakhir pada directori DockerCompose yang kita buat diawal tadi. buat file dengan nama docker-compose.yml
	```
	version: '2'
	services:
  		biodata-service:
    		build: ./biodata
    		volumes:
      			- ./biodata:/usr/src/app
    		ports:
      			- 5001:80
  		website:
    		image: php:apache
    		volumes:
      			- ./website:/var/www/html
    		ports:
      			- 5000:80
    		depends_on:
      			- biodata-service
	```
