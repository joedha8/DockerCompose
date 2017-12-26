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
