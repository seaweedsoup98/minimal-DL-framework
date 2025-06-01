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
        Parameter,
        Function,
        using_config,
        no_grad,
        # test_mode,
        as_array,
        as_variable,
        setup_variable,
        Config,
    )
    from dezero.layers import Layer
    from dezero.models import Model
    # from dezero.datasets import Dataset
    # from dezero.dataloaders import DataLoader, SeqDataLoader
    
    # import dezero.datasets
    # import dezero.dataloaders
    import dezero.optimizers
    import dezero.functions
    # import dezero.functions_conv
    import dezero.layers
    import dezero.utils
    import dezero.cuda
    # import dezero.transforms


setup_variable()