var TodoControllers = angular.module('RegisterControllers', []);

TodoControllers.controller('RegisterListCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.students = [];
    $scope.channel = 'registration';

    $dragon.onReady(function() {
            $dragon.subscribe('student', $scope.channel, {}).then(function(response) {
	                $scope.dataMapper = new DataMapper(response.data);
	            });
    
            $dragon.getList('student').then(function(response) {
		    	console.log(response.data);
	                $scope.students = response.data;
	            });
        });

    $dragon.onChannelMessage(function(channels, message) {
            if (indexOf.call(channels, $scope.channel) > -1) {
	                $scope.$apply(function() {
					console.log("Recieved Message");
			                $scope.dataMapper.mapData($scope.students, message);
			            });
	            }
        });

    $scope.itemDone = function(item) {
            item.done = true != item.done;
            $dragon.update('student', item);
        }
}]);
