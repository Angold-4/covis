// ========================================
// XYVis.js 
//
// A library for visualizing data in 2D
// Two inputs: x and y
// x: str key -> Float32Array
// y: str key -> Float32Array

var XYPlot = function XYPlot(s) {

  this.x = {};
  this.y = {};

  this.sne_x = {};
  this.sne_y = {};

  // prototype chain: 
  // XYVis -> Container -> ViseElement -> Object

  // # 1. Call the parent constructor, select this div
  BasicVis.Container.call(this, s); // set this.s
  // 's' stands for selector

  var W = parseInt(this.s.style('width'));

  // # 2. Add a new div inside for scatter plot
  this.scatter = this.new_child(BasicVis.ScatterPlot);
  this.scatter.div.size([W*(1-3/20)*2/3, W*(1-3/20)*2/3]);
  // initiate scatter plot
  this.scatter
    .N(0)
    .size(4)
    .enable_zoom()
    .color(function(i){return d3.hsl(360*mnist_ys[i]/10.0,0.5,0.5);});

  // # 3. Add a new selection inside
  this.select = this.inner.append("select"); // append select area inside

  var this_ = this;

  // # 4. set handle function for selection
  this.select.on("change", function() {
    this_.display(this.value);
  });
};

XYPlot.prototype = Object.create(BasicVis.Container.prototype);

XYPlot.prototype.data = function data(x, y) {
  this.select.html("");
  this.x = x;
  this.y = y;

  for (var key in x) {
    var inp = this.select
      .append("option")
        .attr("value", key)
        .text(key);
  }

  // keys are the same
  var key0 = Object.keys(x)[0];
  this.display(key0);
  var this_=this;
}

XYPlot.prototype.display = function display(i) {
  /*
  console.log("this x:", this.x)
  console.log("this y:", this.y)

  console.log("i:", i) // key
  console.log("this x i:", this.x[i])
  console.log("this y i:", this.y[i])
  */

  this.sne_x = this.x[i];
  this.sne_y = this.y[i];

  /*
  console.log("this sne x:", this.sne_x)
  console.log("this sne y:", this.sne_y)
  */

  var this_ = this;

  var ax = 1.05*d3.min(this_.sne_x), bx = 1.05*d3.max(this_.sne_x);
  var ay = 1.05*d3.min(this_.sne_y), by = 1.05*d3.max(this_.sne_y);

  // console.log("ax:", ax, "bx:", bx, "ay:", ay, "by:", by)

  // boundary 0.05

  this.scatter // update the scatter
    .N(2000)
    .xrange([ax,bx])
    .yrange([ay,by])
    .x(function(i) {return this_.sne_x[i];})
    .y(function(i) {return this_.sne_y[i];});

  this.scatter.update(); // this.layout(); this.render()
  //this.scheduleUpdate();
}

XYPlot.prototype.child_layout = function child_layout() {

  W = parseInt(this.s.style('width'));

  var margin  = W/20;
  var main    = W - 3*margin;
  var plot    = 2/3*main;
  var side    = 1/3*main;

  this.inner
      .style('width',  W)
      .style('height', plot);

  this.scatter.div
      .style("border", "1px solid black")
      .pos([side + 2*margin, 0])
      .size([plot, plot]);

  this.select
      .style("position", "absolute")
      .style("width", side)
      .style("left", margin)
      .style("top", 0)
      .style("height", plot)
      .attr("multiple", "multiple");

  return this;
}

//===============

var xy_x_set = {}; // define a global var
var xy_y_set = {}; // define a global var

(function() {
  // perform sorting

  // add reps to xy_set
  var rep_names_x = Object.keys(rand_scatters_x).sort();
  var rep_names_y = Object.keys(rand_scatters_y).sort();

  for (var i in rep_names_x){
    var name = rep_names_x[i];
    xy_x_set[name] = rand_scatters_x[name];
  }

  for (var i in rep_names_y){
    var name = rep_names_y[i];
    xy_y_set[name] = rand_scatters_y[name];
  }
})();
