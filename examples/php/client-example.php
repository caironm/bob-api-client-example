<?php

    $url = "https://1-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v1/bob/createaccount";

    require_once('otphp/lib/otphp.php');

    $totp = new \OTPHP\TOTP("R3A7PZLCUQIJFUGX", array('interval' => 90));

    $token = $totp->now();

    $data = json_encode(array(
       'Agreement'             => 'true',
       'EmailAddress'          => 'darthvader@sithorder.net',
       'FirstName'             => 'Anakin',
       'PaternalLastName'      => 'Skywalker',
       'MaternalLastName'      => 'Unknown',
       'GradeNumber'           => '5',
       'Origin'                => 'upn',
       'Password'              => '0123456789',
       'PhoneNumber'           => '000-76543210',
       'UserName'              => 'darthvader@sithorder.net'
    ));

    $headers = array(
      'Accept: application/json',
      'Content-Type: application/json',
      'BobUniversity: upn',
      "BobToken: $token"
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
