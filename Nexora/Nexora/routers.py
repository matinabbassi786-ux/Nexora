class AppDatabaseRouter:

    app_databases = {
        "API": "api",
        "Home": "Home",
        "Student": "Student",
        "Teacher": "Teacher",
        "Notifications": "Notifications",
        "Communication": "Communication",
        "Education": "Education",
        "Bank": "Bank",
    }

    def db_for_read(self, model, **hints):
        return self.app_databases.get(
            model._meta.app_label,
            "default"
        )

    def db_for_write(self, model, **hints):
        return self.app_databases.get(
            model._meta.app_label,
            "default"
        )

    def allow_relation(self, obj1, obj2, **hints):
        return obj1._state.db == obj2._state.db

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        target_db = self.app_databases.get(app_label, "default")
        return db == target_db