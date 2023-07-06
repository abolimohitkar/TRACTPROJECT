window.onload=init; 
function init(){
    const map=new ol.Map
({
    view:new ol.View({
        center:[8214512.255543357, 2098637.109891612],
        zoom:7,
        maxZoom:10,
        minZoom:4 
}),

target:'js-map'
})
const openStreetMapStandard = new ol.layer.Tile({
    source:new ol.source.OSM(),
    visible:true,
    title:'OSMStandard'

})

const openStreetMapHumanitarian = new ol.layer.Tile({

    source:new ol.source.OSM({
        url:'https://{a-c}.title.openstreetmap.fr/hot/{z}/{x}/{y}.png'
    }),
    visible: false,
    title:'OSMHumanitarian'
})
const stamenTerrain= new ol.layer.Tile({
    source:new ol.source.XYZ({
        url:"http://title.stamen.com/terrain/{z}/{x}/{y}.jpg",
        attributions:'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>'
}),
visible:true,
title:'StamenTerrain'

})
//layer group
const  baseLayerGroup=new ol.layer.Group({
    layers:[openStreetMapStandard,openStreetMapHumanitarian,stamenTerrain]
})
map.addLayer(baseLayerGroup);
//layer switcher logics for  basemaps
const baseLayerElements=document.querySelectorAll('.sidebar> input[type=radio]');

for (let baseLayerElement   of  baseLayerElements){
    baseLayerElement.addEventListener('change',function(){
     let baseLayerElementvalue=this.value;
     baseLayerGroup.getLayers().forEach(function(element,index,array){

        let baseLayerTitle=element.get('title');
        element.setVisible(baseLayetTitle===baseLayerElementvalue);
        console.log('baseLayerTitle:'+baseLayerTitle,'baseLayerElementvalue:'+baseLayerElementvalue );
        

     })
        
     })
  //vector layer
  const fillstyle=new ol.style.Fill({
    color:[84,118,255,1]

  })
  const strokeStyle=new ol.style.Stroke({
    color:[46,45,45,1],
    width:1.2
  })
  const circleStyle=new ol.style.Circle({
    fill:new ol.style.Fill({
        color:[245,49,5,1],
        

    }),
    radius:7,
    stroke:strokeStyle
    
  })
  const abcdGeoJSON=new ol.layer.VectorImage({

    source:new ol.source.Vector({
        url:".openlayer_web_map/geojasondata/abcd.geojson",
        format: new ol.format.GeoJSON()
    }),
    visible:true,
    title:'abcdGeoJSON',
    style:new ol.style.Style({
        fill:fillstyle,
        stroke:strokeStyle,
        image:circleStyle
    })

  })
  map.addLayer(abcdGeoJSON);
   

}


}