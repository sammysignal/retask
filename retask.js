UserProfiles = new Meteor.Collection('userprofile');


Router.map(function () {
  this.route('home', {
    path: '/',
    data: function () {return Session.user}
  });
});

if (Meteor.isClient) {
}

if (Meteor.isServer) {
  Router.onBeforeAction(Iron.Router.bodyParser.urlencoded({
    extended: false
  }));
}