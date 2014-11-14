<?php

    $url = "https://3-dot-api-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v3/bob/createaccount";

    $data = json_encode(array(
       'Agreement'             => 'true',
       'EmailAddress'          => 'darthvader@sithorder.net',
       'FirstName'             => 'Anakin',
       'PaternalLastName'      => 'Skywalker',
       'MaternalLastName'      => 'Unknown',
       'GradeNumber'           => '5',
       'Origin'                => 'UPN',
       'Password'              => '0123456789',
       'PhoneNumber'           => '000-76543210',
       'UserName'              => 'darthvader@sithorder.net'
    ));

    $resp = CallAPI("POST", $url, $data);

    var_dump($resp);

    function CallAPI($method, $url, $data) {
        $curl = curl_init();

        $headers = array('Accept: application/json', 'Content-Type: application/json');

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
