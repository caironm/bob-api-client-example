<?php

    // This is the url to the create account method for the QA environment
    $url = "https://1-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v1/bob/createaccount";

    /* These two variables will be sent in custom headers in every requesto to Bob,
       they are unique for Orienta, the BobKey will be different in production */
    $bobuniversity = "aiep";
    $bobkey = "066bf4cb-4f6d-4d73-88dc-339d32170d88";

    $headers = array(
      'Accept: application/json',
      'Content-Type: application/json',
      "BobUniversity: $bobuniversity",
      "BobKey: $bobkey"
    );

    /* This is the data required by Bob, all other data can be stored locally in Orienta data stores,
       this call may be made before or after creating the account locally, whatever suits best Orienta needs */
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

    /* The service will return a response in json format similar to the following:

       Accepted account example:

        {
            "Message": "ACEPTADO",
            "PortfolioID": "20692602",
            "Reason": ["Nuevo usuario creado"],
            "EmailAddress": "dvader@sithorder.net",
            "IsDuplicate": "false",
            "RedirectURL": "http://laureate.careercruising.com/Default/Laureate?PortfolioId=20692602&LaureateRedirect=true",
            "TemporaryPassword": "",
            "UserName": "dvader@sithorder.net"
        }

       Rejected account example:

        {
            "Message": "RECHAZADO",
            "PortfolioID": "20692602",
            "Reason": ["Este Usuario ya existe en nuestro sistema"],
            "EmailAddress": "dvader@sithorder.net",
            "IsDuplicate": "true",
            "RedirectURL": "",
            "TemporaryPassword": "",
            "UserName": "dvader@sithorder.net"
        }

        Based on this your code should then create the account locally in your systems and after that you should call the
        Confirmation method to signal Bob to finish inner processes associated to this account creation, this confirmation
        should be made in both cases, when the account is ACEPTADO or RECHAZADO.

        */
    $resp = CallAPI("POST", $url, $data, $headers);

    // This is merely used for debugging locally, can be safely removed
    var_dump($resp);

?>
