from datetime import datetime, timezone
import os
import requests
import json
import csv

def main():
    offset = 0
    page_size = 200

    provider_count_url = "https://services5.arcgis.com/ACaLB9ifngzawspq/ArcGIS/rest/services/VaccineProviderLocations/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=true&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=0&resultRecordCount=200&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token="

    provider_count = int(json.loads(requests.get(provider_count_url).text)["count"])

    field_names = ["OBJECTID", "ProviderNa", "Address", "City", "State", "Zip", "County", "Phone", "Website", "PfizerTota", "ModernaTot", "OrgGroup", "Allocation", "COVID_ID", "Provider_P"]

    os.makedirs("output", exist_ok=True)
    output_file_name = f"./output/providers-{datetime.now(timezone.utc).isoformat()}.csv"

    with open(output_file_name, mode='w') as output_file:
        providers_writer = csv.writer(output_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        providers_writer.writerow(field_names)

        while (offset < provider_count): 
            page = json.loads(requests.get(provider_info_url(offset, page_size)).text)["features"]
            offset += page_size

            for provider in page:
                provider_attributes = provider["attributes"]
                row = []
                for field in field_names:
                    field_value = str(provider_attributes[field]).replace('\n', ' ')
                    row.append(field_value)
                providers_writer.writerow(row)

def provider_info_url(offset, page_size):
    return f"https://services5.arcgis.com/ACaLB9ifngzawspq/ArcGIS/rest/services/VaccineProviderLocations/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset={offset}&resultRecordCount={page_size}&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token="

if __name__ == '__main__':
    main()
