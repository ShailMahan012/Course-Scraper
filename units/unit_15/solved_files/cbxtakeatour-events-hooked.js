'use strict';if(typeof window.CBXTAKEATOUR_FILTERS!=='undefined'){var retryCounter=0;var $ga_go=!1;function cbxtakeatour_check_ga_loaded($){if((typeof ga==='function'&&ga.loaded)||retryCounter++>5){var $ga_exists=(typeof ga==='function'&&ga.loaded)?!0:!1;$ga_go=$ga_exists}else{setTimeout(cbxtakeatour_check_ga_loaded($),500)}}
function cbxtakeatour_track($,$element,$step_id,tour){var $ga_enable=parseInt(cbxtakeatourpro.ga_enable);if($ga_enable){cbxtakeatour_check_ga_loaded($)}
if($ga_go&&cbxtakeatourpro.track_tour_start){ga('send','event','cbxtakeatour','click',$element.attr('title'),{transport:'beacon',nonInteraction:parseInt(cbxtakeatourpro.track_pbr)?!0:!1})}
if(cbxtakeatourpro.track_log){var data={'action':'cbxtakeatour_track_log','security':cbxtakeatourpro.nonce,'tour_id':$step_id};$.post(cbxtakeatourpro.ajaxurl,data,function(response){response=$.parseJSON(response)})}}
CBXTakeatourEvents_add_action('cbxtakeatour_tour_onStart',cbxtakeatour_track,10)}