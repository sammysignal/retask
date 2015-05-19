UserProfiles = new Meteor.Collection('userprofile');

Router.map(function () {
  this.route('home', {
    path: '/',
    data: function () {
      console.log(this.params);
      return ({
        'username': Session.user,
        'login-fields': this.params.query
      });
    }
  });
});

if (Meteor.isClient) {
}

if (Meteor.isServer) {
  Router.onBeforeAction(Iron.Router.bodyParser.urlencoded({
    extended: false
  }));
}