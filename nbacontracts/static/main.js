drawGraph('points', 'Points Per Game');

var options = {
    points: 'Points Per Game',
    minutes: 'Minutes Per Game',
    field_goal_made: 'Field Goals Made Per Game',
    field_goal_attempted: 'Field Goals Attempted Per Game',
    field_goal_percentage: 'Field Goal %',
    three_point_made: '3 Point Made Per Game',
    three_point_attempted: '3 Point Attempted Per Game',
    three_point_percentage: '3 Point %',
    free_throw_made: 'Free Throws Made Per Game',
    free_throw_attempted: 'Free Throws Attempted Per Game',
    free_throw_percentage: 'Free Throw %',
    offensive_rebounds: 'Offensive Rebounds Per Game',
    defensive_rebounds: 'Defensive Rebounds Per Game',
    total_rebounds: 'Rebounds Per Game',
    assists: 'Assists Per Game',
    steals: 'Steals Per Game',
    blocks: 'Blocks Per Game',
    turnovers: 'Turnovers Per Game',
    efficiency: 'Efficiency',
    wins: 'Team Wins',
    losses: 'Team Losses',
    win_percentage: 'Team Win Percentage',
};

var dropdown = document.getElementById('stat_options');
var fragment = document.createDocumentFragment();

Object.keys(options).forEach(function(key) {
    var opt = document.createElement('option');
    opt.innerHTML = options[key];
    opt.value = key;
    fragment.appendChild(opt)
});

dropdown.appendChild(fragment);

function updateGraph() {
    var stat = dropdown.options[dropdown.selectedIndex].value;
    var label = options[stat];
    document.querySelector('svg').remove();
    document.querySelector('.tooltip').remove();
    drawGraph(stat, label);
}
