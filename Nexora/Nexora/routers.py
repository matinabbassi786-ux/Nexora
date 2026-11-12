
class AppDatabaseRouter:
    """
    All related Nexora Django models use one database.

    This allows normal ForeignKey, OneToOneField
    and ManyToManyField relationships between apps.
    """

    def db_for_read(self, model, **hints):
        return "default"

    def db_for_write(self, model, **hints):
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return (
            obj1._state.db == "default"
            and obj2._state.db == "default"
        )

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == "default"
