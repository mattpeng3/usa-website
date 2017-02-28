var app = angular.module('courseList', ['ngAnimate'])
app.controller('SettingsController1', function($scope) {

  $scope.courses = [];

  $scope.addCourse = function(item) {
  	for (i = 0; i < ($scope.courses).length; i++) {
		  if (item.currentTarget.getAttribute("data-id") == $scope.courses[i]["name"]) {   
		    return;
   		}
   	}
    $scope.courses.push({name: item.currentTarget.getAttribute("data-id"), desc: item.currentTarget.getAttribute("data-desc"), link: item.currentTarget.getAttribute("data-link")});
   	console.log($scope.courses);
  };

  $scope.removeCourse = function(item) {
    for (i = 0; i < $scope.courses.length; i++) {
      if (item.currentTarget.getAttribute("data-id") == $scope.courses[i]["name"]) {
        $scope.courses.splice(i, 1);
      }
    }
  }
});

app.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);