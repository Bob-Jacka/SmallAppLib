import inspect


class Testing:

    @staticmethod
    def run_test(test_class):
        """
        Run method for running tests in given class.
        Ignores init function in class, if exists.
        """
        instance_of_test_class = test_class()
        methods = [name for name, value in
                   inspect.getmembers(test_class, inspect.isfunction) if
                   name != '__init__']  # turn on test mode

        # Main cycle for run tests
        for method in methods:
            getattr(instance_of_test_class, method)
