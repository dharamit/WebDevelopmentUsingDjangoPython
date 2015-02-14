function Hello($scope, $http) {
    $http.get('http://127.0.0.1:8000/api/posts').
        success(function(data) {
            $scope.posts = data;
        });
}
