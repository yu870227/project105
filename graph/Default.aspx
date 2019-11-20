<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js">
</script>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title></title>
     <style>

        .axis path,
        .axis line {
            fill: none;
            stroke: black;
            shape-rendering: crispEdges;
        }

        .axis text {
            font-family: sans-serif;
            font-size: 11px;
        }
        .mouse {
        cursor:pointer
        }
        body {font: 10pt arial;}
        div.tooltip {	
            position: absolute;			
            text-align: left;			
            width: 150px;					
            height: 33px;					
            padding: 2px;				
            font: 12px sans-serif;		
            background: white;	
            border: solid;	
            border-width:1px;	
            border-radius: 5px;			
            pointer-events: none;           			

            overflow:hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
}
    </style>
    <style type="text/css">
        .Panel {
            float: left;
            margin-left: 0px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div style="height: 154px">
            <asp:Panel CssClass="Panel" ID="Panel1" runat="server" Width="332px" Height="111px">
                
            <asp:Label ID="Label1" runat="server" Text="查詢資料：" Font-Size="Large"></asp:Label><asp:TextBox ID="TextBox1" runat="server" Font-Size="Medium" Height="16px" Width="166px"></asp:TextBox>
                <asp:CheckBoxList ID="CheckBoxList1" runat="server" AutoPostBack="True" OnSelectedIndexChanged="CheckBoxList1_SelectedIndexChanged" RepeatDirection="Horizontal" Font-Size="Large">
                    <asp:ListItem Value="0">可讀度</asp:ListItem>
                    <asp:ListItem Value="1">豐富度</asp:ListItem>
                    <asp:ListItem Value="2">即時度</asp:ListItem>
                </asp:CheckBoxList>
                <br />
                <asp:Button ID="Button1" runat="server" Text="查詢" OnClick="Button1_Click" Font-Size="Medium" Height="23px" Width="50px"></asp:Button>
                <br />
                <br />
            </asp:Panel>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:Panel CssClass="Panel" ID="Panel2" runat="server" Width="492px" Height="148px">
                <asp:CheckBox ID="CheckBox1" runat="server" AutoPostBack="True" OnCheckedChanged="CheckBox1_CheckedChanged" Text="依時間查詢" Font-Size="Large" />

                <asp:Panel CssClass="Panel" ID="Panel3" runat="server" Visible="False" Width="489px">
                    <asp:Label ID="Label2" runat="server" Text="開始日期：" Font-Size="Large"></asp:Label><asp:DropDownList ID="DropDownList1" runat="server" AutoPostBack="True" OnSelectedIndexChanged="DropDownList1_SelectedIndexChanged" Font-Size="Medium" Height="28px">
                        <asp:ListItem>選擇年分</asp:ListItem>
                        <asp:ListItem Value="2009">2000</asp:ListItem>
                        <asp:ListItem Value="2009">2001</asp:ListItem>
                        <asp:ListItem Value="2009">2002</asp:ListItem>
                        <asp:ListItem Value="2009">2003</asp:ListItem>
                        <asp:ListItem Value="2009">2004</asp:ListItem>
                        <asp:ListItem Value="2009">2005</asp:ListItem>
                        <asp:ListItem Value="2009">2006</asp:ListItem>
                        <asp:ListItem Value="2009">2007</asp:ListItem>
                        <asp:ListItem Value="2009">2008</asp:ListItem>
                        <asp:ListItem Value="2009">2009</asp:ListItem>
                        <asp:ListItem Value="2010">2010</asp:ListItem>
                        <asp:ListItem Value="2011">2011</asp:ListItem>
                        <asp:ListItem Value="2012">2012</asp:ListItem>
                        <asp:ListItem>2013</asp:ListItem>
                        <asp:ListItem>2014</asp:ListItem>
                        <asp:ListItem>2015</asp:ListItem>
                        <asp:ListItem>2016</asp:ListItem>
                        <asp:ListItem>2017</asp:ListItem>
                        <asp:ListItem>2018</asp:ListItem>
                        <asp:ListItem>2019</asp:ListItem>
                    </asp:DropDownList>
                    &nbsp;<asp:Label ID="Label3" runat="server" Text="年" Font-Size="Large"></asp:Label><asp:DropDownList ID="DropDownList2" runat="server" Enabled="False" Font-Size="Medium" Height="28px">
                        <asp:ListItem>選擇月份</asp:ListItem>
                        <asp:ListItem>1</asp:ListItem>
                        <asp:ListItem>2</asp:ListItem>
                        <asp:ListItem>3</asp:ListItem>
                        <asp:ListItem>4</asp:ListItem>
                        <asp:ListItem>5</asp:ListItem>
                        <asp:ListItem>6</asp:ListItem>
                        <asp:ListItem>7</asp:ListItem>
                        <asp:ListItem>8</asp:ListItem>
                        <asp:ListItem>9</asp:ListItem>
                        <asp:ListItem>10</asp:ListItem>
                        <asp:ListItem>11</asp:ListItem>
                        <asp:ListItem>12</asp:ListItem>
                    </asp:DropDownList>
                    <asp:Label ID="Label4" runat="server" Text="月" Font-Size="Large"></asp:Label></asp:Panel>
                <br />
              
                <asp:CheckBox ID="CheckBox2" runat="server" AutoPostBack="True" Text="學校來源" Font-Size="Large" />
                <br />
                <asp:CheckBox ID="CheckBox3" runat="server" AutoPostBack="True" Text="醫院來源" Font-Size="Large" />
                <br />
                <asp:CheckBox ID="CheckBox4" runat="server" AutoPostBack="True" Text="研究院來源" Font-Size="Large" />
            </asp:Panel>

        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:Button ID="Button2" runat="server" OnClick="Button2_Click1" Text="返回主畫面" Width="137px" Font-Size="Medium" />

        </div>

        <script src="http://d3js.org/d3.v4.min.js"></script>
        <script src="https://d3js.org/d3-color.v1.min.js"></script>
        <script src="https://d3js.org/d3-interpolate.v1.min.js"></script>
        <script src="https://d3js.org/d3-scale-chromatic.v1.min.js"></script>
        <script src="graph2.js"></script>
        <script src="graph3.js"></script>

        <script type="text/javascript">

            function drawVisualization(dataset, xv, yv) {
                //畫布周邊的空白
                //var padding = 20;
                var padding = { left: 30, right: 30, top: 20, bottom: 20 };
                //畫布大小
                var w = 1040 - padding.left - padding.right;
                var h = 340 - padding.top - padding.bottom;
                var s, x, y;

                //在body裡添加一個SVG畫布
                var svg = d3.select("body")
                            .append("svg")
                            .attr("width", w)
                            .attr("height", h)
                            .on("mouseover", function () { return tooltip.style("visibility", "visible"); })
                            .on("mousemove", function () { return tooltip.style("top", (event.pageY - 10) + "px").style("left", (event.pageX - 150) + "px"); })
                            .on("mouseout", function () { return tooltip.style("visibility", "hidden"); });
                var tooltip = d3.select("body")
                                .append("div")
                                .style("position", "absolute")
                                .style("z-index", "10")
                                .style("visibility", "hidden")
                                .text("滾動滑鼠可縮放");
                //zoom axis
                var zoom = d3.zoom()
                             //.scaleExtent([1, 1000])
                             .scaleExtent([1, 5000])
                             .on("zoom", zoomed);
                svg.call(zoom);
                //x軸的比例尺
                var xScale = d3.scaleLinear()
                               //.domain([0, d3.max(dataset, function (d) { return d[0]; })])
                               .domain([0, 10])
                               .range([padding.left, w - padding.left - padding.right]);
                //Y軸的比例尺
                var yScale = d3.scaleLinear()
                               //.domain([0, d3.max(dataset, function (d) { return d[1]; })])
                                 .domain([0, 1])
                                 .range([h - padding.top, padding.bottom]);
                dataset.forEach(function (d) {
                    d.x = +d.x;
                    d.y = +d.y;
                });
                var div = d3.select("body")
                            .append("div")
                            .attr("class", "tooltip")
                            .style("opacity", 0);
                //點 
                var circles = svg.selectAll("circle")
                                .data(dataset)
                                /*.data("tooltip", function (circles) {
                                    return xv + ':<b>' + circles.x
                                })*/
                                .enter()
                                .append("circle")
                                .classed("mouse", true)
                                .attr("cx", function (d) {
                                    //return xScale(d[0]);
                                    return xScale(d.x);
                                })
                                .attr("cy", function (d) {
                                    //return yScale(d[1]);
                                    return yScale(0.05);
                                })
                                .attr("fill", "#7dc1ff")
                                .attr("fill-opacity", 1)
                                .attr("r", 8)
                                .on('mouseover', function (d) {
                                    d3.select(this)
                                    .attr("r", 10)
                                    div.transition()
                                       .duration(200)
                                       .style("opacity", .9);


                                    if (d.x == 10) {
                                        div.html(d.name + "<br>" + xv + ":★★★★★★★★★★")
                                       .style("left", (d3.event.pageX - 10) + "px")
                                   //.style("top", (d3.event.pageY -28) + "px");
                                       .style("top", (d3.event.pageY - 40) + "px");
                                       //.style("color", "#ff0000");
                                    }
                                    else if (d.x < 10 && d.x >= 9) {
                                        div.html(d.name + "<br>" + xv + ":★★★★★★★★★☆")
                                        .style("left", (d3.event.pageX - 10) + "px")
                                    //.style("top", (d3.event.pageY -28) + "px");
                                        .style("top", (d3.event.pageY - 40) + "px");
                                        //.style("color", "#ff8400");
                                    }
                                    else if (d.x < 9 && d.x >= 8) {
                                        div.html(d.name + "<br>" + xv + ":★★★★★★★★☆☆")
                                       .style("left", (d3.event.pageX - 10) + "px")
                                   //.style("top", (d3.event.pageY -28) + "px");
                                       .style("top", (d3.event.pageY - 40) + "px");
                                       //.style("color", "#ffff00");
                                    }
                                    else if (d.x < 8 && d.x >= 7) {
                                        div.html(d.name + "<br>" + xv + ":★★★★★★★☆☆☆")
                                        .style("left", (d3.event.pageX - 10) + "px")
                                    //.style("top", (d3.event.pageY -28) + "px");
                                        .style("top", (d3.event.pageY - 40) + "px");
                                        //.style("color", "#84ff00");
                                    }
                                    else if (d.x < 7 && d.x >= 6) {
                                        div.html(d.name + "<br>" + xv + ":★★★★★★☆☆☆☆")
                                       .style("left", (d3.event.pageX - 10) + "px")
                                   //.style("top", (d3.event.pageY -28) + "px");
                                       .style("top", (d3.event.pageY - 40) + "px");
                                       //.style("color", "##00ff55");
                                    }
                                    else if (d.x < 6 && d.x >= 5) {
                                        div.html(d.name + "<br>" + xv + ":★★★★★☆☆☆☆☆")
                                       .style("left", (d3.event.pageX - 10) + "px")
                                   //.style("top", (d3.event.pageY -28) + "px");
                                       .style("top", (d3.event.pageY - 40) + "px");
                                       //.style("color", "#00ffdd");
                                    }
                                    else if (d.x < 5 && d.x >= 4) {
                                        div.html(d.name + "<br>" + xv + ":★★★★☆☆☆☆☆☆")
                                       .style("left", (d3.event.pageX - 10) + "px")
                                   //.style("top", (d3.event.pageY -28) + "px");
                                       .style("top", (d3.event.pageY - 40) + "px");
                                       //.style("color", "#0080ff");
                                    }
                                    else if (d.x < 4 && d.x >= 3) {
                                        div.html(d.name + "<br>" + xv + ":★★★☆☆☆☆☆☆☆")
                                       .style("left", (d3.event.pageX - 10) + "px")
                                   //.style("top", (d3.event.pageY -28) + "px");
                                       .style("top", (d3.event.pageY - 40) + "px");
                                       //.style("color", "#0d00ff");
                                    }
                                    else if (d.x < 3 && d.x >= 2) {
                                        div.html(d.name + "<br>" + xv + ":★★☆☆☆☆☆☆☆☆")
                                       .style("left", (d3.event.pageX - 10) + "px")
                                   //.style("top", (d3.event.pageY -28) + "px");
                                       .style("top", (d3.event.pageY - 40) + "px");
                                       //.style("color", "#a600ff");
                                    }
                                    else if (d.x < 2 && d.x >= 1) {
                                        div.html(d.name + "<br>" + xv + ":★☆☆☆☆☆☆☆☆☆")
                                       .style("left", (d3.event.pageX - 10) + "px")
                                   //.style("top", (d3.event.pageY -28) + "px");
                                       .style("top", (d3.event.pageY - 40) + "px");
                                       //.style("color", "#ff00bf");
                                    }
                                    else {
                                        div.html(d.name + "<br>" + xv + ":☆☆☆☆☆☆☆☆☆☆")
                                       .style("left", (d3.event.pageX - 10) + "px")
                                   //.style("top", (d3.event.pageY -28) + "px");
                                       .style("top", (d3.event.pageY - 40) + "px");
                                       //.style("color", "#000000");
                                    }


                                })
                                .on('mouseout', function () {
                                    d3.select(this)
                                    .attr("r", 8)
                                    div.transition()
                                       .duration(500)
                                    .style("opacity", 0);
                                })
                                //click事件
                                .on('click', function (circles) {
                                    //window.location.assign(circles.url);
                                    window.open(circles.url);
                                    d3.select(this)
                                    .attr("fill", "#9999ff")
                                });
                //點文字
                var t = svg.selectAll("text")
                          .data(dataset)
                          .append("text")
                          .text(function (d) {
                              return d.x;
                          })
                          .attr("x", function (d) {
                              return xScale(d.x);
                          })
                          .attr("font-family", "sans-serif")
                          .attr("font-size", "11px")
                          .attr("fill", "black");
                //定義座標軸
                var xAxis = d3.axisBottom(xScale);
                var x_axis = svg.append("g")
                                .attr("transform", "translate(0,280)")
                                .call(xAxis);
                svg.append("g")
                   .append("text")
                   .text(xv)
                   .attr("font-size", "16px")
                   .attr("transform", "translate(930,285)");

                //繪製新座標軸與點
                function zoomed() {
                    var newxScale = d3.event.transform.rescaleX(xScale);
                    x_axis.transition()
                          .duration(0)
                          .call(xAxis.scale(newxScale));
                    circles.attr("cx", function (d) {
                        return newxScale(d.x)
                    });
                    t.attr("x", function (d) {
                        return newxScale(d.x)
                    });
                }

                //回到原比例
                d3.select('#reset').on('click', function () {
                    d3.transition()
                      .duration(250)
                      .tween("zoom", function () {
                          var si = d3.interpolate(s, 1);
                          var xi = d3.interpolate(x, 1);
                          var yi = d3.interpolate(y, 1);
                          return function (t) {
                              svg.call(zoom.translate([xi(t), yi(t)]).scale(si(t)).event);
                          }
                      })
                })
                var container = document.getElementById('graph');
            }

            function graph2D(dataset, xv, yv, name) {
                window.onload = function () {
                    var chart = new CanvasJS.Chart("graph", {
                        animationEnabled: true,
                        zoomEnabled: true,
                        height: 500,
                        axisX: {
                            title: xv,
                            minimum: 0,
                            maximum: 10
                        },
                        axisY: {
                            title: yv,
                            minimum: 0,
                            maximum: 10
                        },
                        toolTip: {
                            contentFormatter: function (e) {
                                var xpoint = "", ypoint = "";
                                for (var i = 1; i < e.entries[0].dataPoint.x; i++) {
                                    xpoint = xpoint + "★";
                                }
                                for (var i = 1; i < e.entries[0].dataPoint.y; i++) {
                                    ypoint = ypoint + "★";
                                }
                                return "標題:</b>" + e.entries[0].dataPoint.name + "<br>" + xv + ":<b>" + xpoint + "<br>" + yv + ":<b>" + ypoint;

                            }
                        },
                        data: [{
                            type: "scatter",
                            color: "#7dc1ff",
                            markerSize: 15,
                            //toolTipContent: "標題:" + "</b> {name}<br/" + "<b>" + xv + " </b>:{x} <br/>" + "<b>" + yv + "</b>:{y} <br/>" + "<b>",
                            //"<b>" + xv + " </b>:{x} <br/>" + "<b>" + yv + "</b>:{y}",
                            dataPoints: dataset,
                            click: onClick
                        }]
                    });
                    function onClick(e) {
                        //window.location.assign(e.dataPoint.url);
                        window.open(e.dataPoint.url);
                        e.dataPoint.color = "#9999ff";
                        chart.render();
                    };
                    chart.render();
                }
            }

            var graph = null;
            function drawVisualization3(data, xv, yv, zv, a) {
                // specify options
                var options = {
                    width: '1200px',
                    height: '600px',
                    style: 'dot-color',
                    //dataColor: '#3267D2',
                    //dotSizeRatio:'0.04',
                    showPerspective: true,
                    showGrid: true,
                    showShadow: false,

                    // Option tooltip can be true, false, or a function returning a string with HTML contents
                    //tooltip: true,
                    tooltip: function (point) {
                        // parameter point contains properties x, y, z
                        //return '標題:<b>' + point.h + '<br/>' + xv + ': <b>' + point.x + '<br/>' + yv + ':<b>' + point.y + '<br/>' + zv + ':<b>' + point.z;
                        var xstring = "", ystring = "", zstring = "";
                        for (var i = 1; i < point.x; i++) {
                            xstring = xstring + "★";
                        }
                        for (var i = 1; i < point.y; i++) {
                            ystring = ystring + "★";
                        }
                        for (var i = 1; i < point.z; i++) {
                            zstring = zstring + "★";
                        }
                        return '標題:<b>' + point.h + '<br/>' + xv + ': <b>' + xstring + '<br/>' + yv + ':<b>' + ystring + '<br/>' + zv + ':<b>' + zstring;
                    },
                    onclick: function (point) {

                        for (var dot in a) {
                            if (a[dot].id == point.id) {
                                //alert(a[dot]);
                                a[dot].style = "#9999FF";
                                break;
                            }
                        }
                        data = new vis.DataSet();
                        data.add(a);
                        window.open(point.url);
                        drawVisualization3(data, xv, yv, zv, a);
                    },
                    xLabel: xv,
                    yLabel: yv,
                    zLabel: zv,
                    xValueLabel: function (value) {
                        return value;
                    },
                    yValueLabel: function (value) {
                        return value;
                    },
                    zValueLabel: function (value) {
                        return value;
                    },
                    keepAspectRatio: true,
                    verticalRatio: 0.5
                };
                var camera = graph ? graph.getCameraPosition() : null;
                // Instantiate our graph object.
                var container = document.getElementById('graph');
                graph = new vis.Graph3d(container, data, options);
                if (camera) graph.setCameraPosition(camera); // restore camera position

            }


            function graph1(xv, yv, sel) {
                dataset = [];
                dataset = JSON.parse(sel);
                drawVisualization(dataset, xv, yv);
            }

            function graph2(xv, yv, sel, name) {
                var dataset = [];
                //data = new CanvasJS.
                dataset = JSON.parse(sel);
                graph2D(dataset, xv, yv, name);
            }
            function graph3(xv, yv, zv, sel) {
                //alert(sel)
                var data = null;
                data = new vis.DataSet();
                a = JSON.parse(sel);
                data.add(a);
                drawVisualization3(data, xv, yv, zv, a);
            }

            function chose_one() {
                alert("至少選擇一個!!!");
            }
            function alertnodata() {
                alert("No Data!!Sorry");
            }
            function nosearch() {
                alert("請輸入關鍵字");
            }
            function alertshow(str) {
                alert(str);
            }
            $(document).ready(function () {
                $("#divProgress").hide();
                $("#Button1").click(function () {
                    $("#divProgress").show();
                });
            });
        </script>
        <div id="graph">

            <div id="divProgress" runat="server" style=" display: none; text-align: center; position: fixed; top: 50%; left: 50%;">
                <asp:Image ID="imgLoading" runat="server" ImageUrl="~/loading.gif" />
                <br />
                <font color="#1B3563" size="2px">資料處理中</font>
            </div>
        </div>
    </form>
</body>
</html>
