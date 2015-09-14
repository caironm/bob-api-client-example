<?php

    // This is the url to the profile update method for the QA environment
    $url = "https://1-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v1/bob/profileupdate";

    /* These two variables will be sent in custom headers in every requesto to Bob,
       they are unique for Orienta, the BobKey will be different in production */
    $bobuniversity = "aiep";
    $bobkey = "066bf4cb-4f6d-4d73-88dc-339d32170d88";

    $headers = array(
      'Accept: application/json',
      'Content-Type: application/json',
      'BobUniversity: $bobuniversity',
      "BobKey: $bobkey"
    );

    /* This Portfolio ID was provided by the response of the Create Account method,  */
    $portfolioid = "1234567890";

    /* The email of the user that changed status */
    $email = "dvader@sithorder.net";

    /* This variable is true if the user changed status from being a prospect to being a student */
    $enrolled = true;

    $data = json_encode(array(
       'EmailAddress'          => $email,
       'PortfolioID'           => $portfolioid,
       'Enrolled'              => $enrolled
    ));

    // boilerplate code to invoke the service
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

    /* This is an optional method used to notify Bob when a prospect turned into a student */
    $resp = CallAPI("POST", $url, $data, $headers);

    // This is merely used for debugging locally, can be safely removed
    var_dump($resp);

?>
