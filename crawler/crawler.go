package crawler

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
)

type DWListing struct {
	id            string   `json:"id"`
	title         string   `json:"title"`
	address       string   `json:"id"`
	totalRent     float32  `json:"price"`
	heatingCosts  float32  `json:"heatingCosts"`
	area          float32  `json:"area"`
	numberofRooms float32  `json:"rooms"`
	floor         float32  `json:"level"`
	images        []string `json:"images"`
	url           string
	geolocation   []string `json:"id"`
}

func GetDegewoListings() []byte {

	req, err := http.NewRequest("GET", "https://immosuche.degewo.de/de/search.json?utf8=%E2%9C%93&property_type_id=1&categories%5B%5D=1&property_number=&address%5Braw%5D=&address%5Bstreet%5D=&address%5Bcity%5D=&address%5Bzipcode%5D=&address%5Bdistrict%5D=&district=&price_switch=false&price_switch=on&price_from=&price_to=&price_from=&price_to=&price_radio=null&price_from=&price_to=&qm_radio=null&qm_from=&qm_to=&rooms_radio=null&rooms_from=&rooms_to=&features%5B%5D=&wbs_required=&order=rent_total_without_vat_asc&", nil)
	if err != nil {
		log.Println(err)
	}
	req.Header.Set("Authority", "immosuche.degewo.de")
	req.Header.Set("Pragma", "no-cache")
	req.Header.Set("Cache-Control", "no-cache")
	req.Header.Set("Sec-Ch-Ua", "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"")
	req.Header.Set("Accept", "application/json, text/javascript, */*; q=0.01")
	req.Header.Set("X-Requested-With", "XMLHttpRequest")
	req.Header.Set("Sec-Ch-Ua-Mobile", "?0")
	req.Header.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36")
	req.Header.Set("Sec-Ch-Ua-Platform", "\"macOS\"")
	req.Header.Set("Sec-Fetch-Site", "same-origin")
	req.Header.Set("Sec-Fetch-Mode", "cors")
	req.Header.Set("Sec-Fetch-Dest", "empty")
	req.Header.Set("Referer", "https://immosuche.degewo.de/de/search?size=10&page=1&property_type_id=1&categories%5B%5D=1&lat=&lon=&area=&address%5Bstreet%5D=&address%5Bcity%5D=&address%5Bzipcode%5D=&address%5Bdistrict%5D=&address%5Braw%5D=&district=&property_number=&price_switch=true&price_radio=null&price_from=&price_to=&qm_radio=null&qm_from=&qm_to=&rooms_radio=null&rooms_from=&rooms_to=&wbs_required=&order=rent_total_without_vat_asc")
	req.Header.Set("Accept-Language", "en-US,en;q=0.9")
	req.Header.Set("Cookie", "deg_expose_marked=[]; _pk_id.2.5bbb=a28e2af57f5fe6eb.1644520044.; cookie-tracking=decline; cookie-marketing=accept; cookie-maps=accept; cookie-immo=accept; cookie-youtube=accept; degewo-cookie-consent=true; TS0194984b=01fe90c44264fcdb94e6fe68f16311d117d8e29c7eb3a1dffed5c1029dff0d0826433165743db1d1886469b7c2346e8f22ecf0a1de; _pk_ref.2.5bbb=%5B%22%22%2C%22%22%2C1647816865%2C%22https%3A%2F%2Fwww.degewo.de%2F%22%5D; _pk_ses.2.5bbb=1; _immo-search_session=VFNPRnVJZ082b21Sa2ZzWExRV1NSeWt3d3Z6S1YxVzZCZkk2Mi9EanRia1ZjejI2a0tidklhNHhJSDMrbjAvU201TFB4WUZQMjg5QlRhMDg4eGtocEk5T0dGV2VReDR2TFY1UitDL0E2NkxWNHNySFE3bU1Ecng3aXM5SDl1dDRCdFpmOWFwOEZCSjBMOTF6SnRSU2s5ZXJlKzcyOUkvSWE2ZW5XTmRKbkRHcnNVcU9tRTFhaVkyaFVJd3ptK0ZYZW9jYi9xaVowcFJhUGdzWFBVTFlQemxoL05qd3dQOE96MG1aSG9sY2F2aDRRaHE3eUFJYnBRYXgybDF5WkE2NHRCTVRNRmZOR3k1cEpnSUxVZzlGeXdEc2p2R1llNkFad1A3WW1Dc3ozZ1U1MFArK1F0S1pSUHhsck1ZcHNFakgrT3p3VzIxS21Jd205THlpOWJVN29TMytDYVBEVEgvZDlERFVQZTdta0pFQ0JKN1BVemRvUyt3bFdtaUJKbm1Lbk4rNGtoUUlNOXlGaEFNTzF2K1VEUTVVbG4xbi9TY20zTzdjRnIxS2xrQm1nanExRmxDaFJYWk1BYXBWQWpsZCtBdkdOTVNjT3FjMitEZExkNTNnTmFPMlFKZDZsdlhndTRPR1FMOVlEbU1zbVJuMDArTW5hTmNNVTNvUzVISyt1YmZFUE5uUmZVUDl4anJ3SzBZNGRFd3krd09kYzluMDg3WXJXdEZ6QUY4Z3dsZ3JhWVF0RWNPK2l5Z2YxUTJ5RXJsT1paZmVFc2ljRFJCNmZDUzRvaUdha3hiWDNHWXloRktPVWtvMWo3YTh6L3ZPZjFDSms5cThpbVVLcHoyaXBiMDJnVmwrWXMzZzh2WDNSWTVnY2w5NTJDWVJTdFlocDlTU2NxeFRuVDRDUlRrM2VyQkFUSXFuK3JQREFGclU5TVVpSTU3ay93SGVRWVNLUmdzZ0FReFhJaUJzakhTTkxyNDlndDRpSjRKY3dwOXdHS0JMc1BEM3lSZm9tWnRqOSs2OEZBbXdTNnpNQlpoMDVPcC8zMmhCaVgzQTExTkIraUNUQVBFRU1BWT0tLTFvc2JNWlFFWk4yTHhScFM4UHR5TWc9PQ%3D%3D--efbc59ee3cc3367f499c5de13d7a91140b64805a")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Println(err)
	}
	output, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Println(err)
	}
	// newOutput := string(output)

	defer resp.Body.Close()

	return output

}

func GetDWListings() []byte {

	body := strings.NewReader("{\"infrastructure\":{},\"flatTypes\":{},\"other\":{},\"commercializationType\":\"rent\",\"utilizationType\":\"flat\",\"location\":\"Berlin\",\"city\":\"Berlin\",\"locale\":\"de\"}")
	req, err := http.NewRequest("POST", "https://immo-api.deutsche-wohnen.com/estate/findByFilter", body)
	if err != nil {
		log.Println(err)
	}
	req.Header.Set("Authority", "immo-api.deutsche-wohnen.com")
	req.Header.Set("Pragma", "no-cache")
	req.Header.Set("Cache-Control", "no-cache")
	req.Header.Set("Sec-Ch-Ua", "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"")
	req.Header.Set("Accept", "*/*")
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
	req.Header.Set("Sec-Ch-Ua-Mobile", "?0")
	req.Header.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36")
	req.Header.Set("Sec-Ch-Ua-Platform", "\"macOS\"")
	req.Header.Set("Origin", "https://www.deutsche-wohnen.com")
	req.Header.Set("Sec-Fetch-Site", "same-site")
	req.Header.Set("Sec-Fetch-Mode", "cors")
	req.Header.Set("Sec-Fetch-Dest", "empty")
	req.Header.Set("Accept-Language", "en-US,en;q=0.9")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Println(err)
	}

	output, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Println(err)
	}

	// newOutput := string(output)
	// newOutput = strings.ReplaceAll(newOutput, "[", "")
	// newOutput = strings.ReplaceAll(newOutput, "]", "")

	defer resp.Body.Close()

	return output
}

func ProcessJSON() {
	degewo := GetDegewoListings()
	// fmt.Println(degewo)

	var result map[string]interface{}
	json.Unmarshal(degewo, &result)

	immos := result["immos"]

	fmt.Println(result["immos"])
	// fmt.Println(result[0])

	for key, value := range immos {
		fmt.Println(key, value.(string))
	}
}
