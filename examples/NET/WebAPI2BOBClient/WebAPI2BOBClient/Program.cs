using System;
using System.Net.Http;
using System.Net.Http.Formatting;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using System.Collections.Generic;
using WebAPI2BOBClient.Models;
using Newtonsoft.Json;

namespace WebAPI2BOBClient
{
    class Program
    {
        static void Main(string[] args)
        {
            var portfolio = "";

            if (args.Length == 1)
            {
                portfolio = args[0];
            }
            else 
            {
                var rnd = new Random();

                portfolio = rnd.Next(1, 999999999).ToString();
            }

            Console.WriteLine("Updating Portfolio ID: {0}...", portfolio);

            RunAsync(portfolio).Wait();
        }

        static async Task RunAsync(string portfolio)
        {
            using (var client = new HttpClient())
            {
                client.DefaultRequestHeaders.Accept.Clear();
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

                var account = new CompletionUpdateModel()
                {
                    PortfolioID = portfolio,
                    MMDate = "2013/10/15",
                    Cluster1 = "AC",
                    Cluster2 = "AB",
                    ResultURL = "http://cc/" + portfolio,
                    PhoneNumber = "5556667777",
                    TerminosCC = "1"
                };

                var BOB_SECRET_KEY = "VY72IUVROA6LTYHK";

                var totp = new OTPNet.TOTP(BOB_SECRET_KEY, 90);

                var jsonFormatter = new JsonMediaTypeFormatter();

                var content = new ObjectContent<CompletionUpdateModel>(account, jsonFormatter);

                var url = "https://1-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v1/bob/completionupdate";
                // var url = "http://192.168.1.103:8080/_ah/api/bob/v1/bob/completionupdate";

                var requestUri = new Uri(url);

                var request = new HttpRequestMessage()
                {
                    RequestUri = requestUri,
                    Method = HttpMethod.Post,
                    Content = content
                };

                request.Content.Headers.ContentType = new MediaTypeWithQualityHeaderValue("application/json");
                request.Headers.Add("BobUniversity", "cc");

                var code = totp.now();

                request.Headers.Add("BobToken", code.ToString());

                var response = client.SendAsync(request).Result;

                Console.WriteLine("HTTP status code: {0}", response.StatusCode.ToString());

                if (response.IsSuccessStatusCode)
                {
                    var jsonString = await response.Content.ReadAsStringAsync();

                    var caresponse = JsonConvert.DeserializeObject<CompletionUpdateResponseModel>(jsonString);

                    Console.WriteLine("Codigo: {0}", caresponse.Codigo);
                    Console.WriteLine("Mensaje: {0}", caresponse.Mensaje);
                }
            }
        }
    }
}
