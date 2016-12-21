function drawGraph(xField, xLabel){

    var domain = window.location.hostname == 'localhost' ?
        'localhost:5000' :
        window.location.hostname;
    var margin = { top: 10, right: 20, bottom: 55, left: 55 };
    var width = 550 - margin.left - margin.right;
    var height = 550 - margin.top - margin.bottom;

    var tooltip = d3.select("body").append("div")
        .attr("class", "tooltip")
        .style("opacity", 0)
        .style("z-index", 2)
        .style("width:", "100%");

    var svg = d3.select('.chart')
      .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .call(responsivefy)
      .append('g')
        .attr('transform', 'translate(' + margin.left + ', ' + margin.top + ')');

    d3.json('//'+domain+'/api/data', function(err, data) {
        var yScale = d3.scaleLinear()
            .domain([0, d3.max(data, d => parseFloat(d.salary_2016_17.replace(/,|\$/g, '')))])
            .range([height, 0])
            .nice();
        var yAxis = d3.axisLeft(yScale)
            .ticks(10, "s")
            .tickPadding(3);

        svg.call(yAxis);

        var xScale = d3.scaleLinear()
            .domain([0, d3.max(data, d => d[xField])])
            .range([0, width])
            .nice();

        var xAxis = d3.axisBottom(xScale)
            .ticks(5)
            .tickPadding(3);
        svg
        .append('g')
          .attr('transform', `translate(0, ${height})`)
        .call(xAxis);

        var circles = svg
          .selectAll()

        var circles = svg
          .selectAll('.ball')
          .data(data)
          .enter()
          .append('g')
          .on("mouseover", function(d) {
                tooltip.transition()
                    .duration(200)
                    .style("opacity", .9);
                tooltip .html("<span>Player: <br>"+d.name+"</span><br><br><span>Salary: <br>"+
                                d.salary_2016_17+"</span><br><br><span>"+
                                xLabel+": <br>"+d[xField]+"</span>")
                    .style("left", (d3.event.pageX + 10) + "px")
                    .style("top", (d3.event.pageY - 35) + "px");
                })
          .on("mouseout", function(d) {
              tooltip.transition()
                  .duration(500)
                  .style("opacity", 0);
          })
          .attr('class', 'ball')
          .attr('transform', d => {
            return `translate(
                ${xScale(d[xField])},
                ${yScale(parseFloat(d.salary_2016_17.replace(/,|\$/g, '')))})`;
          });

        circles
          .append('circle')
          .attr('cx', 0)
          .attr('cy', 0)
          .attr('r', 6)
          .style('fill', 'steelblue')
          .style('opacity', '0.6');

        // text label for x axis
        svg.append('text')
          .attr("transform",
              "translate(" + (width/2) + " ," +
                             (height + margin.top + 30) + ")")
          .attr("fill", "black")
          .style("text-anchor", "middle")
          .style("font-size", "18px")
          .text(xLabel+" 2015/16");

        // text label for y-axis
        svg.append('text')
          .attr("transform", "rotate(-90)")
          .attr("y", 0 - margin.left)
          .attr("x",0 - (height / 2))
          .attr("dy", "1em")
          .attr("fill", "black")
          .style("text-anchor", "middle")
          .style("font-size", "18px")
          .text("Salary 2016/17");
    });
}

function responsivefy(svg) {
    // get container + svg aspect ratio
    var container = d3.select(svg.node().parentNode),
        width = parseInt(svg.style("width")),
        height = parseInt(svg.style("height")),
        aspect = width / height;

    // add viewBox and preserveAspectRatio properties,
    // and call resize so that svg resizes on inital page load
    svg.attr("viewBox", "0 0 " + width + " " + height)
        .attr("preserveAspectRatio", "xMinYMid")
        .call(resize);

    // to register multiple listeners for same event type,
    // you need to add namespace, i.e., 'click.foo'
    // necessary if you call invoke this function for multiple svgs
    // api docs: https://github.com/mbostock/d3/wiki/Selections#on
    d3.select(window).on("resize." + container.attr("id"), resize);

    // get width of container and resize svg to fit it
    function resize() {
        var targetWidth = parseInt(container.style("width"));
        svg.attr("width", targetWidth);
        svg.attr("height", Math.round(targetWidth / aspect));
    }
}
