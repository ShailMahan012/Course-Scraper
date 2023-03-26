richSnippet=function(opts){function isEmpty(variable){return!(typeof variable!='undefined'&&variable.length>0)}
var request=new XMLHttpRequest();var api="https://api-cache.reviews.co.uk";if(opts.site){if(opts.site=='io'){api="https://api.reviews.io"}}else if(document.currentScript&&(src=document.currentScript.src)){if(src.indexOf('.co.uk')==-1){api="https://api.reviews.io"}}
var mode=!isEmpty(opts.sku)||!isEmpty(opts.mpn)||!isEmpty(opts.asProduct)?'Product':'LocalBusiness';var d=autoMergeRS(mode);if(d!=!1){opts.data=d}
request.onreadystatechange=function(){if(this.readyState===4){if(this.status>=200&&this.status<400){var data=this.responseText;var scriptTag=document.createElement("script");if(opts.data&&opts.store!='driftworks-com'){reviews=JSON.parse(data);reviews=richSnippetRecursiveMerge(reviews,opts.data);data=JSON.stringify(reviews)}
if(data!=''){scriptTag.setAttribute("type","application/ld+json");scriptTag.appendChild(document.createTextNode(data));document.getElementsByTagName("head")[0].appendChild(scriptTag)}}}};if(isEmpty(opts.sku)&&isEmpty(opts.mpn)&&((typeof opts.internal!='undefined'&&parseInt(opts.internal)==1)||opts.store=='mr-clutch-autocentres-ltd')){request.open('GET',api+'/json-ld/merchant/richsnippet?store='+opts.store,!0);request.send()}else if(isEmpty(opts.sku)&&!isEmpty(opts.asProduct)){request.open('GET',api+'/json-ld/merchant/richsnippet?store='+opts.store+'&asProduct='+encodeURIComponent(opts.asProduct),!0);request.send()}else if(!isEmpty(opts.sku)||!isEmpty(opts.mpn)){var url=api+'/json-ld/product/richsnippet';var queryString='store='+opts.store+'&sku='+(opts.sku?encodeURIComponent(opts.sku):'')+'&data='+(!!opts.data?encodeURIComponent(!0):encodeURIComponent(!1))+'&mpn='+(opts.mpn?encodeURIComponent(opts.mpn):'');if(opts.enable_syndication==!0){queryString+='&enable_syndication=true'}else if(opts.enableSyndication==!0){queryString+='&enable_syndication=true'}
if(queryString.length>2000){request.open('POST',url,!0);request.setRequestHeader("Content-type","application/x-www-form-urlencoded");request.send(queryString)}else{request.open('GET',url+'?'+queryString,!0);request.send()}}
request=null};autoMergeRS=function(mode){var existing=findJsonLDSnippets(mode);if(existing==!1){existing=findMicroDataSnippets(mode)}
return existing}
getMicroDataItem=function(i){var item={};item.name=i.getAttribute('itemprop');if(i.tagName=='IMG'){item.value=i.getAttribute('src')}else if(i.hasAttribute('content')){item.value=i.getAttribute('content')}else{item.value=i.innerText}
return item}
findMicroDataSnippets=function(mode){var snip=document.querySelector('[itemtype="http://schema.org/'+mode+'"]');if(snip){var json=parseMicroData(snip);return json.json}
return!1}
parseMicroData=function(element){var pr=!1;var json={};var properties=element.querySelectorAll('[itemprop]');var label='';for(var x=0;x<properties.length;x++){if(properties[x].getAttribute('itemprop')=='http://schema.org/Review'||properties[x].getAttribute('itemprop')=='http://schema.org/AggregateRating'){}else if(properties[x].hasAttribute('itemscope')){label=properties[x].getAttribute('itemprop')?properties[x].getAttribute('itemprop'):properties[x].getAttribute('itemtype');if(label!='itemListElement'&&label!='position'&&label!='item'){pr=parseMicroData(properties[x]);json[label]=pr.json;x+=pr.skip}}else{pr=getMicroDataItem(properties[x]);if(pr.name!='position'&&pr.name!='item'){json[pr.name]=pr.value}}
properties[x].removeAttribute('itemprop')}
element.removeAttribute('itemtype');element.removeAttribute('itemprop');element.removeAttribute('itemscope');return{json:json,skip:x}}
findJsonLDSnippets=function(mode){var jsons=document.querySelectorAll('script[type="application/ld+json"]');var json='';for(var i=0;i<jsons.length;i++){jsonTemp=jsons[i].innerHTML.trim().replace(/[\t\n]/g,'');json=JSON.parse(jsonTemp);if(json['@type']&&json['@type']==mode){var childDOM=jsons[i];childDOM.parentNode.removeChild(childDOM);return json}}
return!1}
richSnippetRecursiveMerge=function(obj1,obj2){for(var p in obj2){try{if(obj2[p].constructor==Object){obj1[p]=richSnippetRecursiveMerge(obj1[p],obj2[p])}else{obj1[p]=obj2[p]}}catch(e){obj1[p]=obj2[p]}}
return obj1};if(typeof richSnippetCallback=='function'){richSnippetCallback()}