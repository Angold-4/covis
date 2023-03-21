//=========================

// customized fn for CDB data
function display_cdb(data, type, div, fix_width) {

  // "type" specify whether it is CDB1 or CDB3

  // hard-coded local variables
  var col0 = "個股代號／公司名字" // for CDB1
  var col1 = "行業"               // for CDB3

  var col2 = "時富雷達 (CR)"
  var col3 = "基本分析比重"
  var col4 = "技術分析比重"

  var col5 = "基本分析分數"
  var col6 = "技術分析分數"

  var col7 = "相對強弱指數 RSI（9天）"
  var col8 = "波幅指數 Volatility（10天）"
  var col9 = "平均線 SMA（10天）"
  var col10 = "銷售額增長标准分数"
  var col11 = "債務股本比例标准分数"
  var col12 = "淨收入改善标准分数"
  var col13 = "資本回報标准分数"
  var col14 = "保留盈餘增長标准分数"
  var col15 = "TA4"
  var col16 = "TA5"
  var col17 = "移動平均線标准分数"
  var col18 = "相對強弱指數标准分数"
  var col19 = "布林线指标标准分数"

  var headers = data['headers']; // headers

  // default var1 and var2: col5, col6
  var var1 = col5, var2 = col6;

  var col01;
  if (type == "CDB1") {
    col01 = col1;
  } else if (type == "CDB3") {
    col01 = col0;
  } else {
    // for now, only CDB1 and CDB3 are supported
    // so return
    console.log("Invalid type: " + type + " for CDBVis.js")
    return;
  }

  var name_values = [], name_values_tmp = [], cr_values = [], cr_values_tmp = [];
  var var1_values = [], var2_values = [], var1_values_tmp = [], var2_values_tmp = [];
 
  var1_values_tmp = data[var1];
  var2_values_tmp = data[var2];
  name_values_tmp = data[col01];
  cr_values_tmp = data[col2]; // Cash Radar Points

  // perform some data cleaning
  // the empty data will not be displayed

  for (var i = 0; i < var1_values_tmp.length; i++) {
    if (var1_values_tmp[i] != "" && var2_values_tmp[i] != "" && name_values_tmp[i] != "" && cr_values_tmp[i] != "") {
      // only all of them are not empty, then push
      var1_values.push(var1_values_tmp[i]);
      var2_values.push(var2_values_tmp[i]);
      name_values.push(name_values_tmp[i]);
      cr_values.push(cr_values_tmp[i]);
    }
  }

  console.log("var1_values: " + var1_values);
  console.log("var2_values: " + var2_values);
  console.log("name_values: " + name_values);
  console.log("cr_values: " + cr_values);

  /*
  var sne = data["vs_sne"];
  var toks = data["toks"];
  var urls = data["urls"];
  var cats = data["cats"];
  var tok_cats = data["tok_cats"];
  */

  div = d3.select(div); // select this div

  var this_ = this;

  var W = parseInt(div.style('width'));

  class_N = 2; // x and y

  this_.categories = []; // array

  var opacity = 0.2 + 0.4*Math.pow(0.01, Math.max(1, var1_values.length - 3000)/20000.0);
  // console.log(opacity, sne.length, Math.max(1, sne.length - 3000)/20000.0);

  console.log("length: ", Math.min(var1_values.length, var2_values.length))

  // init a scatter plot
  var scatter = new BasicVis.ScatterPlot(div.select(".sne"))
    .N(Math.min(var1_values.length, var2_values.length))
    .enable_zoom()
    .xrange.fit(var1_values)
    .yrange.fit(var2_values)
    .x(function(i) {return var1_values[i];})
    .y(function(i) {return var2_values[i];})
    .size(2.3)
    .color(function(i){
      var k = -1;
      /* uncolored first (TODO: handle coloring by CR)
      if (tok_cats[i]) {
        for (var catn in this_.categories) {
          if (tok_cats[i].indexOf(this_.categories[catn]) != -1) {k = catn;}
        }
      }
      */
      if (k == -1) { return "rgba(150,150,150," + opacity + ")"; }
      return d3.hsl(360*k/class_N,0.5,0.5);
    }
  );

  scatter.bindToWindowResize()

  this.scatter = scatter;

  /*
  scatter.recolor = function() {
      var data = scatter._data;
      scatter.points
        .attr('fill', data.color);
  };
  */

  scatter.update();


  // display the details whenever the mouse is scroll over it
  // TODO: handle tooltip (subclass)

  this_.tooltip = new BasicVis.CDBTextTooltip();

  this_.tooltip._CR = cr_values;
  this_.tooltip._name_values = name_values;
  this_.tooltip._var1_values = var1_values;
  this_.tooltip._var2_values = var2_values;
  this_.tooltip._var1 = var1;
  this_.tooltip._var2 = var2;

  this_.tooltip.bind(scatter.points);
  this_.tooltip.bind_move(scatter.s);
  this_.tooltip.div.style("font-size", "85%");
  if (fix_width) {
    this_.tooltip.div.style('width', W/2 + "px");
  }

  /*
  if (urls) {
    scatter.points.on("click", function(i){
      window.open(urls[i]);
      // TODO: open it at bottom
    });
  }
  */

  var category_div_container = function(cont) {

    function new_cat_div (cdn) {
      var n = this_.categories.length;
      var inner = $("<div>").appendTo(cont).css("margin-bottom", "10px");
      var sq = $("<div>").appendTo(inner);
      sq.css("width", "10%").css("height", "15px").css("display", "inline-block");
      sq.css("background-color", "hsl(" + 360*n/class_N + ",50%,50%)" );
      var div = $("<input>").appendTo(inner);
      div.css("display", "inline-block");
      div.css("width", "80%");
      div.css("margin-left", "5%")
      div.css("font-size", "90%");
      //$("<br>").appendTo(cont);
      div.cdn = cdn; // create a new property (cdn) x or y
      category_div(div); // bind the cat
      // cdn stands for cooridnate name (x or y)
    }

    var filtering = function() {
      // helper function (must update va1 and var2 first)
      var1_values = [];
      var2_values = [];
      var1_values_tmp = data[var1];
      var2_values_tmp = data[var2];
      name_values_tmp = data[col01];
      cr_values_tmp = data[col2]; // Cash Radar Points

      // perform some data cleaning
      // the empty data will not be displayed

      for (var i = 0; i < var1_values_tmp.length; i++) {
        if (var1_values_tmp[i] != "" && var2_values_tmp[i] != "" && name_values_tmp[i] != "" && cr_values_tmp[i] != "") {
          // only all of them are not empty, then push
          var1_values.push(var1_values_tmp[i]);
          var2_values.push(var2_values_tmp[i]);
          name_values.push(name_values_tmp[i]);
          cr_values.push(cr_values_tmp[i]);
        }
      }
    }

    var category_div = function(div){
      // we need to know which coordinate this div is for (cdn)

      /*
      var n = this_.categories.length;
      this_.categories.push("");
      */

      // handle fn (change the x/y coordinate)
      catChange = function(e, ui, cdn){
        if (ui && ui.item && ui.item.value) {
          var s = ui.item.value || this.value;
        } else {
          var s = this.value;
        }

        if (headers.indexOf(s) == -1 && s != "") return;

        // we got a valid header
        // then set the x and y

        // var header = headers.indexOf(s); // the index of the header

        if (div.cdn == 0) {
          var1 = s;
          filtering();
        } else if (div.cdn == 1) {
          var2 = s;
          filtering()
        } else {
          console.log("CDBVis.js: Unknown coordinate: " + cdn);
          return;
        }

        scatter // update the scatter
          .N(Math.min(var1_values.length, var2_values.length))
          .enable_zoom()
          .xrange.fit(var1_values)
          .yrange.fit(var2_values)
          .x(function(i) {return var1_values[i];})
          .y(function(i) {return var2_values[i];})

        scatter.update(); // this.layout(); this.render()

        this_.tooltip._CR = cr_values;
        this_.tooltip._name_values = name_values;
        this_.tooltip._var1_values = var1_values;
        this_.tooltip._var2_values = var2_values;
        this_.tooltip._var1 = var1;
        this_.tooltip._var2 = var2;

        // setTimeout(function() {scatter.recolor();}, 0);
        //if (this_.categories.length == n + 1 && s != "")
        //  new_cat_div();
      }

      var getMatchList = function(req, resp) {
        var term = req.term;
        var max_matches = 12;
        if (term.length == 0) {
          var matches = headers.slice(0, max_matches);
          if (headers.length > max_matches){
            matches.push('...');
          }
        } else {
          // input some characters
          var term_esc = term;
          var regex = new RegExp(term_esc, 'i'); //ignore case
          var matches = [];
          for (var i = 0; i < headers.length; i++) {
            if (!regex.test(headers[i]))
              continue;
            matches.push(headers[i]);
            if (matches.length >= max_matches) {
              matches.push('...');
              break;
            }
          }
        }
        resp(matches);
      }

      div.autocomplete({
        delay: 1,
        source: getMatchList,
        select: catChange,
        change: catChange
      });

      div.change(catChange);
    }
    
    // only call this when first start
    for (var j = 0; j < class_N; j++) {
      new_cat_div(cdn=j); // init
    }

    setTimeout(function() {
      var H_main = parseInt(div.style("height"));
      var H_cont = parseInt(cont.style("height"));
      cont.style("top", (H_main-H_cont)/2 + "px")
    }, 1);

  }

  // set the category_div_container
  category_div_container(div.select(".legend"));
  $(".ui-autocomplete").css("font-size", "90%").css("text-align", "left");
}
