@prefix asgs: <http://linked.data.gov.au/def/asgs#> .
@prefix data: <http://linked.data.gov.au/def/datatype/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix geox: <http://linked.data.gov.au/def/geox#> .
@prefix ns1: <http://purl.org/linked-data/registry#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://linked.data.gov.au/dataset/asgs2016/destinationzone/511221403> a asgs:DestinationZone ;
    asgs:contains <http://linked.data.gov.au/dataset/asgs2016/meshblock/50031710000> ;
    asgs:dznCode2016 "511221403" .

<http://linked.data.gov.au/dataset/asgs2016/localgovernmentarea/50490> a asgs:LocalGovernmentArea ;
    asgs:contains <http://linked.data.gov.au/dataset/asgs2016/meshblock/50031710000> ;
    asgs:lgaCode2016 "50490" .

<http://linked.data.gov.au/dataset/asgs2016/naturalresourcemanagementregion/503> a asgs:NaturalResourceManagementRegion ;
    asgs:contains <http://linked.data.gov.au/dataset/asgs2016/meshblock/50031710000> ;
    asgs:nrmrCode2016 "503" .

<http://linked.data.gov.au/dataset/asgs2016/stateorterritory/5> asgs:isStateOrTerritoryOf <http://linked.data.gov.au/dataset/asgs2016/meshblock/50031710000> .

<http://linked.data.gov.au/dataset/asgs2016/statesuburb/51288> a asgs:StateSuburb ;
    asgs:contains <http://linked.data.gov.au/dataset/asgs2016/meshblock/50031710000> ;
    asgs:sscCode2016 "51288" .

<http://linked.data.gov.au/dataset/asgs2016/statisticalarealevel1/50602112225> asgs:isStatisticalAreaLevel1Of <http://linked.data.gov.au/dataset/asgs2016/meshblock/50031710000> .

<http://linked.data.gov.au/dataset/asgs2016/meshblock/50031710000> a asgs:Feature,
        asgs:MeshBlock,
        geo:Feature ;
    asgs:category "Residential" ;
    asgs:mbCode2016 "50031710000" ;
    geox:hasAreaM2 [ data:value 30400.0 ;
            geox:inCRS <http://www.opengis.net/def/crs/EPSG/0/3577> ],
        [ data:value 42412.665305415874 ;
            geox:inCRS <http://www.opengis.net/def/crs/EPSG/0/3857> ] ;
    ns1:register <http://linked.data.gov.au/dataset/asgs2016/meshblock/> ;
    geo:hasGeometry [ a geo:Geometry ;
            geo:asGML """<gml:MultiSurface xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:MB="WFS" xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" srsName="urn:ogc:def:crs:EPSG:6.9:3857">
  <gml:surfaceMember>
    <gml:Polygon>
      <gml:exterior>
        <gml:LinearRing>
          <gml:posList> 12902794.504700001 -3757970.5163999982 12902886.478399999 -3757877.9356999993 12902680.1307 -3757668.7490000017 12902665.726799998 -3757654.1464999989 12902657.5436 -3757662.6539999992 12902619.630199999 -3757700.3423999995 12902607.136100002 -3757687.6403999999 12902569.230799999 -3757725.3311999999 12902563.392099999 -3757739.1667999998 12902690.743700001 -3757865.7820999995 12902794.504700001 -3757970.5163999982</gml:posList>
        </gml:LinearRing>
      </gml:exterior>
    </gml:Polygon>
  </gml:surfaceMember>
</gml:MultiSurface>
"""^^geo:gmlLiteral ] .

