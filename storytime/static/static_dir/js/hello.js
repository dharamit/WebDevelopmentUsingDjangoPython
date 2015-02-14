/*function Hello($scope, $http) {
    $http.get('http://127.0.0.1:8000/api/posts')
        success(function(data) {
            $scope.posts = data;
        });
}*/

(function(){
var app = angular.module('postSite',[]);
app.controller('PostController', ['$scope', function($scope){
	$scope.get = 'amit';
	//this.product = posts;
}]);

var posts = {
	author: "amit",
	title: "book",
}
})();
