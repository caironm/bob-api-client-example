using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace WebAPI2BOBClient.Models
{
    class CompletionUpdateResponseModel
    {
        [JsonProperty("Codigo")]
        public string Codigo { get; set; }

        [JsonProperty("Mensaje")]
        public string Mensaje { get; set; }
    }
}
