UserProfiles = new Meteor.Collection('userprofile');

Router.map(function () {
  this.route('home', {
    path: '/',
    data: function () {
      if (Session.get("user")) {
        return Session.get("user");
      }
      console.log(this);
      console.log(this.params);
      var query = this.params.query
      var name = query.firstname;
      if (name) {
        //Filled out sign up form
      }
      else if (query.email) {
        // Filled out log in form
        usr = UserProfiles.find({username: query.email});
        if (usr.password == query.password) {
          Session.set("user", this.params);
          // redirect to logged in!
        }
        // Assume password changed, attmept API login
      }
      else {
        return (0);
      }
    }
  });
  this.route('logout', {
    template: 'home',
    data: function () {
      Session.set("user", null);
      return(0);
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