<?php

    $url = "https://1-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v1/bob/createaccount";

    $bobuniversity = "orienta";
    $bobkey = "094e3089-91e0-4449-b2d1-1110038ad88c";

    $data = json_encode(array(
       'Agreement'             => 'true',
       'EmailAddress'          => $_POST["email"],
       'FirstName'             => $_POST["first_name"],
       'PaternalLastName'      => $_POST["paternal_lastname"],
       'MaternalLastName'      => $_POST["maternal_lastname"],
       'GradeNumber'           => '5',
       'Origin'                => $bobuniversity,
       'Password'              => $_POST["password"],
       'PhoneNumber'           => $_POST["phone"],
       'UserName'              => $_POST["email"]
    ));

    $headers = array(
      'Accept: application/json',
      'Content-Type: application/json',
      'BobUniversity: $bobuniversity',
      "BobKey: $bobkey"
    );

    var_dump($headers);
    var_dump($data);

    $resp = CallAPI("POST", $url, $data, $headers);

    var_dump($resp);

    function CallAPI($method, $url, $data, $headers) {
        $curl = curl_init();

        curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
        curl_setopt($curl, CURLOPT_POST, true);
        curl_setopt($curl, CURLOPT_URL, $url);
        curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

        $result = curl_exec($curl);

        curl_close($curl);

        return $result;
    }

?>
