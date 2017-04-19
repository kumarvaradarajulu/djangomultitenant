import threading


thread_local_data = threading.local()


class MultiTenant(object):

    @staticmethod
    def _select_db():
        return getattr(thread_local_data, 'tenant_code', 'default')

    def db_for_read(self, model, **hints):
        return self._select_db()

    def db_for_write(self, model, **hints):
        return self._select_db()

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
