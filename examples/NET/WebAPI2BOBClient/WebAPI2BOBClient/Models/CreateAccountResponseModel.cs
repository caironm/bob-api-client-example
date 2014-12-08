using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace WebAPI2BOBClient.Models
{
    class CreateAccountResponseModel
    {
        [JsonProperty("Message")]
        public string Message { get; set; }

        [JsonProperty("PortfolioID")]
        public string PortfolioID { get; set; }

        [JsonProperty("Reason")]
        public List<string> Reason { get; set; }

        [JsonProperty("EmailAddress")]
        public string EmailAddress { get; set; }

        [JsonProperty("IsDuplicate")]
        public string IsDuplicate { get; set; }

        [JsonProperty("RedirectURL")]
        public string RedirectURL { get; set; }

        [JsonProperty("TeporaryPassword")]
        public string TeporaryPassword { get; set; }

        [JsonProperty("UserName")]
        public string UserName { get; set; }
    }
}
