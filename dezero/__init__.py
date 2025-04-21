is_simple_core = False

if is_simple_core:
    from dezero.core_simple import (
        Variable,
        Function,
        using_config,
        no_grad,
        as_variable,
        as_array,
        setup_variable,
    )

else:
    from dezero.core import (
        Variable,
        Function,
        using_config,
        no_grad,
        as_variable,
        as_array,
        setup_variable,
    )


setup_variable()