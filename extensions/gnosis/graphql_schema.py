import sgqlc.types


graphql_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class Batch_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'startEpoch', 'endEpoch', 'solution', 'solutions', 'firstSolutionEpoch', 'lastRevertEpoch', 'txHash')


class BigDecimal(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = graphql_schema


Boolean = sgqlc.types.Boolean

class Bytes(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class Deposit_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'user', 'tokenAddress', 'amount', 'batchId', 'createEpoch', 'txHash')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class OrderDirection(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('asc', 'desc')


class Order_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'owner', 'orderId', 'fromBatchId', 'fromEpoch', 'untilBatchId', 'untilEpoch', 'buyToken', 'sellToken', 'priceNumerator', 'priceDenominator', 'maxSellAmount', 'minReceiveAmount', 'soldVolume', 'boughtVolume', 'trades', 'createEpoch', 'cancelEpoch', 'deleteEpoch', 'txHash', 'txLogIndex')


class Price_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'token', 'batchId', 'priceInOwlNumerator', 'priceInOwlDenominator', 'volume', 'createEpoch', 'txHash')


class Solution_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'batch', 'solver', 'feeReward', 'objectiveValue', 'trades', 'createEpoch', 'revertEpoch', 'txHash', 'txLogIndex')


String = sgqlc.types.String

class Token_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'address', 'fromBatchId', 'symbol', 'decimals', 'name', 'createEpoch', 'txHash')


class Trade_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'order', 'owner', 'sellVolume', 'buyVolume', 'tradeBatchId', 'tradeEpoch', 'buyToken', 'sellToken', 'createEpoch', 'revertEpoch', 'txHash', 'txLogIndex')


class User_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'fromBatchId', 'orders', 'deposits', 'withdrawRequests', 'withdrawals', 'createEpoch', 'txHash')


class WithdrawRequest_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'user', 'tokenAddress', 'amount', 'withdrawableFromBatchId', 'createEpoch', 'createBatchId', 'txHash')


class Withdraw_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'user', 'tokenAddress', 'amount', 'createEpoch', 'createBatchId', 'txHash')



########################################################################
# Input Objects
########################################################################
class Batch_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'start_epoch', 'start_epoch_not', 'start_epoch_gt', 'start_epoch_lt', 'start_epoch_gte', 'start_epoch_lte', 'start_epoch_in', 'start_epoch_not_in', 'end_epoch', 'end_epoch_not', 'end_epoch_gt', 'end_epoch_lt', 'end_epoch_gte', 'end_epoch_lte', 'end_epoch_in', 'end_epoch_not_in', 'solution', 'solution_not', 'solution_gt', 'solution_lt', 'solution_gte', 'solution_lte', 'solution_in', 'solution_not_in', 'solution_contains', 'solution_not_contains', 'solution_starts_with', 'solution_not_starts_with', 'solution_ends_with', 'solution_not_ends_with', 'first_solution_epoch', 'first_solution_epoch_not', 'first_solution_epoch_gt', 'first_solution_epoch_lt', 'first_solution_epoch_gte', 'first_solution_epoch_lte', 'first_solution_epoch_in', 'first_solution_epoch_not_in', 'last_revert_epoch', 'last_revert_epoch_not', 'last_revert_epoch_gt', 'last_revert_epoch_lt', 'last_revert_epoch_gte', 'last_revert_epoch_lte', 'last_revert_epoch_in', 'last_revert_epoch_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    start_epoch = sgqlc.types.Field(BigInt, graphql_name='startEpoch')
    start_epoch_not = sgqlc.types.Field(BigInt, graphql_name='startEpoch_not')
    start_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='startEpoch_gt')
    start_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='startEpoch_lt')
    start_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='startEpoch_gte')
    start_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='startEpoch_lte')
    start_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startEpoch_in')
    start_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startEpoch_not_in')
    end_epoch = sgqlc.types.Field(BigInt, graphql_name='endEpoch')
    end_epoch_not = sgqlc.types.Field(BigInt, graphql_name='endEpoch_not')
    end_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='endEpoch_gt')
    end_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='endEpoch_lt')
    end_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='endEpoch_gte')
    end_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='endEpoch_lte')
    end_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endEpoch_in')
    end_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endEpoch_not_in')
    solution = sgqlc.types.Field(String, graphql_name='solution')
    solution_not = sgqlc.types.Field(String, graphql_name='solution_not')
    solution_gt = sgqlc.types.Field(String, graphql_name='solution_gt')
    solution_lt = sgqlc.types.Field(String, graphql_name='solution_lt')
    solution_gte = sgqlc.types.Field(String, graphql_name='solution_gte')
    solution_lte = sgqlc.types.Field(String, graphql_name='solution_lte')
    solution_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='solution_in')
    solution_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='solution_not_in')
    solution_contains = sgqlc.types.Field(String, graphql_name='solution_contains')
    solution_not_contains = sgqlc.types.Field(String, graphql_name='solution_not_contains')
    solution_starts_with = sgqlc.types.Field(String, graphql_name='solution_starts_with')
    solution_not_starts_with = sgqlc.types.Field(String, graphql_name='solution_not_starts_with')
    solution_ends_with = sgqlc.types.Field(String, graphql_name='solution_ends_with')
    solution_not_ends_with = sgqlc.types.Field(String, graphql_name='solution_not_ends_with')
    first_solution_epoch = sgqlc.types.Field(BigInt, graphql_name='firstSolutionEpoch')
    first_solution_epoch_not = sgqlc.types.Field(BigInt, graphql_name='firstSolutionEpoch_not')
    first_solution_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='firstSolutionEpoch_gt')
    first_solution_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='firstSolutionEpoch_lt')
    first_solution_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='firstSolutionEpoch_gte')
    first_solution_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='firstSolutionEpoch_lte')
    first_solution_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='firstSolutionEpoch_in')
    first_solution_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='firstSolutionEpoch_not_in')
    last_revert_epoch = sgqlc.types.Field(BigInt, graphql_name='lastRevertEpoch')
    last_revert_epoch_not = sgqlc.types.Field(BigInt, graphql_name='lastRevertEpoch_not')
    last_revert_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='lastRevertEpoch_gt')
    last_revert_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='lastRevertEpoch_lt')
    last_revert_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='lastRevertEpoch_gte')
    last_revert_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='lastRevertEpoch_lte')
    last_revert_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='lastRevertEpoch_in')
    last_revert_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='lastRevertEpoch_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')


class Block_height(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('hash', 'number')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(Int, graphql_name='number')


class Deposit_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'user', 'user_not', 'user_gt', 'user_lt', 'user_gte', 'user_lte', 'user_in', 'user_not_in', 'user_contains', 'user_not_contains', 'user_starts_with', 'user_not_starts_with', 'user_ends_with', 'user_not_ends_with', 'token_address', 'token_address_not', 'token_address_in', 'token_address_not_in', 'token_address_contains', 'token_address_not_contains', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'batch_id', 'batch_id_not', 'batch_id_gt', 'batch_id_lt', 'batch_id_gte', 'batch_id_lte', 'batch_id_in', 'batch_id_not_in', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    user = sgqlc.types.Field(String, graphql_name='user')
    user_not = sgqlc.types.Field(String, graphql_name='user_not')
    user_gt = sgqlc.types.Field(String, graphql_name='user_gt')
    user_lt = sgqlc.types.Field(String, graphql_name='user_lt')
    user_gte = sgqlc.types.Field(String, graphql_name='user_gte')
    user_lte = sgqlc.types.Field(String, graphql_name='user_lte')
    user_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_in')
    user_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_not_in')
    user_contains = sgqlc.types.Field(String, graphql_name='user_contains')
    user_not_contains = sgqlc.types.Field(String, graphql_name='user_not_contains')
    user_starts_with = sgqlc.types.Field(String, graphql_name='user_starts_with')
    user_not_starts_with = sgqlc.types.Field(String, graphql_name='user_not_starts_with')
    user_ends_with = sgqlc.types.Field(String, graphql_name='user_ends_with')
    user_not_ends_with = sgqlc.types.Field(String, graphql_name='user_not_ends_with')
    token_address = sgqlc.types.Field(Bytes, graphql_name='tokenAddress')
    token_address_not = sgqlc.types.Field(Bytes, graphql_name='tokenAddress_not')
    token_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenAddress_in')
    token_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenAddress_not_in')
    token_address_contains = sgqlc.types.Field(Bytes, graphql_name='tokenAddress_contains')
    token_address_not_contains = sgqlc.types.Field(Bytes, graphql_name='tokenAddress_not_contains')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigInt, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigInt, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigInt, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigInt, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigInt, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_not_in')
    batch_id = sgqlc.types.Field(BigInt, graphql_name='batchId')
    batch_id_not = sgqlc.types.Field(BigInt, graphql_name='batchId_not')
    batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='batchId_gt')
    batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='batchId_lt')
    batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='batchId_gte')
    batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='batchId_lte')
    batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='batchId_in')
    batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='batchId_not_in')
    create_epoch = sgqlc.types.Field(BigInt, graphql_name='createEpoch')
    create_epoch_not = sgqlc.types.Field(BigInt, graphql_name='createEpoch_not')
    create_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gt')
    create_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lt')
    create_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gte')
    create_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lte')
    create_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_in')
    create_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')


class Order_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'owner', 'owner_not', 'owner_gt', 'owner_lt', 'owner_gte', 'owner_lte', 'owner_in', 'owner_not_in', 'owner_contains', 'owner_not_contains', 'owner_starts_with', 'owner_not_starts_with', 'owner_ends_with', 'owner_not_ends_with', 'order_id', 'order_id_not', 'order_id_gt', 'order_id_lt', 'order_id_gte', 'order_id_lte', 'order_id_in', 'order_id_not_in', 'from_batch_id', 'from_batch_id_not', 'from_batch_id_gt', 'from_batch_id_lt', 'from_batch_id_gte', 'from_batch_id_lte', 'from_batch_id_in', 'from_batch_id_not_in', 'from_epoch', 'from_epoch_not', 'from_epoch_gt', 'from_epoch_lt', 'from_epoch_gte', 'from_epoch_lte', 'from_epoch_in', 'from_epoch_not_in', 'until_batch_id', 'until_batch_id_not', 'until_batch_id_gt', 'until_batch_id_lt', 'until_batch_id_gte', 'until_batch_id_lte', 'until_batch_id_in', 'until_batch_id_not_in', 'until_epoch', 'until_epoch_not', 'until_epoch_gt', 'until_epoch_lt', 'until_epoch_gte', 'until_epoch_lte', 'until_epoch_in', 'until_epoch_not_in', 'buy_token', 'buy_token_not', 'buy_token_gt', 'buy_token_lt', 'buy_token_gte', 'buy_token_lte', 'buy_token_in', 'buy_token_not_in', 'buy_token_contains', 'buy_token_not_contains', 'buy_token_starts_with', 'buy_token_not_starts_with', 'buy_token_ends_with', 'buy_token_not_ends_with', 'sell_token', 'sell_token_not', 'sell_token_gt', 'sell_token_lt', 'sell_token_gte', 'sell_token_lte', 'sell_token_in', 'sell_token_not_in', 'sell_token_contains', 'sell_token_not_contains', 'sell_token_starts_with', 'sell_token_not_starts_with', 'sell_token_ends_with', 'sell_token_not_ends_with', 'price_numerator', 'price_numerator_not', 'price_numerator_gt', 'price_numerator_lt', 'price_numerator_gte', 'price_numerator_lte', 'price_numerator_in', 'price_numerator_not_in', 'price_denominator', 'price_denominator_not', 'price_denominator_gt', 'price_denominator_lt', 'price_denominator_gte', 'price_denominator_lte', 'price_denominator_in', 'price_denominator_not_in', 'max_sell_amount', 'max_sell_amount_not', 'max_sell_amount_gt', 'max_sell_amount_lt', 'max_sell_amount_gte', 'max_sell_amount_lte', 'max_sell_amount_in', 'max_sell_amount_not_in', 'min_receive_amount', 'min_receive_amount_not', 'min_receive_amount_gt', 'min_receive_amount_lt', 'min_receive_amount_gte', 'min_receive_amount_lte', 'min_receive_amount_in', 'min_receive_amount_not_in', 'sold_volume', 'sold_volume_not', 'sold_volume_gt', 'sold_volume_lt', 'sold_volume_gte', 'sold_volume_lte', 'sold_volume_in', 'sold_volume_not_in', 'bought_volume', 'bought_volume_not', 'bought_volume_gt', 'bought_volume_lt', 'bought_volume_gte', 'bought_volume_lte', 'bought_volume_in', 'bought_volume_not_in', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'cancel_epoch', 'cancel_epoch_not', 'cancel_epoch_gt', 'cancel_epoch_lt', 'cancel_epoch_gte', 'cancel_epoch_lte', 'cancel_epoch_in', 'cancel_epoch_not_in', 'delete_epoch', 'delete_epoch_not', 'delete_epoch_gt', 'delete_epoch_lt', 'delete_epoch_gte', 'delete_epoch_lte', 'delete_epoch_in', 'delete_epoch_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains', 'tx_log_index', 'tx_log_index_not', 'tx_log_index_gt', 'tx_log_index_lt', 'tx_log_index_gte', 'tx_log_index_lte', 'tx_log_index_in', 'tx_log_index_not_in')
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'owner', 'owner_not', 'owner_gt', 'owner_lt', 'owner_gte', 'owner_lte', 'owner_in', 'owner_not_in', 'owner_contains', 'owner_not_contains', 'owner_starts_with', 'owner_not_starts_with', 'owner_ends_with', 'owner_not_ends_with', 'order_id', 'order_id_not', 'order_id_gt', 'order_id_lt', 'order_id_gte', 'order_id_lte', 'order_id_in', 'order_id_not_in', 'from_batch_id', 'from_batch_id_not', 'from_batch_id_gt', 'from_batch_id_lt', 'from_batch_id_gte', 'from_batch_id_lte', 'from_batch_id_in', 'from_batch_id_not_in', 'from_epoch', 'from_epoch_not', 'from_epoch_gt', 'from_epoch_lt', 'from_epoch_gte', 'from_epoch_lte', 'from_epoch_in', 'from_epoch_not_in', 'until_batch_id', 'until_batch_id_not', 'until_batch_id_gt', 'until_batch_id_lt', 'until_batch_id_gte', 'until_batch_id_lte', 'until_batch_id_in', 'until_batch_id_not_in', 'until_epoch', 'until_epoch_not', 'until_epoch_gt', 'until_epoch_lt', 'until_epoch_gte', 'until_epoch_lte', 'until_epoch_in', 'until_epoch_not_in', 'buy_token', 'buy_token_not', 'buy_token_gt', 'buy_token_lt', 'buy_token_gte', 'buy_token_lte', 'buy_token_in', 'buy_token_not_in', 'buy_token_contains', 'buy_token_not_contains', 'buy_token_starts_with', 'buy_token_not_starts_with', 'buy_token_ends_with', 'buy_token_not_ends_with', 'sell_token', 'sell_token_not', 'sell_token_gt', 'sell_token_lt', 'sell_token_gte', 'sell_token_lte', 'sell_token_in', 'sell_token_not_in', 'sell_token_contains', 'sell_token_not_contains', 'sell_token_starts_with', 'sell_token_not_starts_with', 'sell_token_ends_with', 'sell_token_not_ends_with', 'price_numerator', 'price_numerator_not', 'price_numerator_gt', 'price_numerator_lt', 'price_numerator_gte', 'price_numerator_lte', 'price_numerator_in', 'price_numerator_not_in', 'price_denominator', 'price_denominator_not', 'price_denominator_gt', 'price_denominator_lt', 'price_denominator_gte', 'price_denominator_lte', 'price_denominator_in', 'price_denominator_not_in', 'max_sell_amount', 'max_sell_amount_not', 'max_sell_amount_gt', 'max_sell_amount_lt', 'max_sell_amount_gte', 'max_sell_amount_lte', 'max_sell_amount_in', 'max_sell_amount_not_in', 'sold_volume', 'sold_volume_not', 'sold_volume_gt', 'sold_volume_lt', 'sold_volume_gte', 'sold_volume_lte', 'sold_volume_in', 'sold_volume_not_in', 'bought_volume', 'bought_volume_not', 'bought_volume_gt', 'bought_volume_lt', 'bought_volume_gte', 'bought_volume_lte', 'bought_volume_in', 'bought_volume_not_in', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'cancel_epoch', 'cancel_epoch_not', 'cancel_epoch_gt', 'cancel_epoch_lt', 'cancel_epoch_gte', 'cancel_epoch_lte', 'cancel_epoch_in', 'cancel_epoch_not_in', 'delete_epoch', 'delete_epoch_not', 'delete_epoch_gt', 'delete_epoch_lt', 'delete_epoch_gte', 'delete_epoch_lte', 'delete_epoch_in', 'delete_epoch_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains', 'tx_log_index', 'tx_log_index_not', 'tx_log_index_gt', 'tx_log_index_lt', 'tx_log_index_gte', 'tx_log_index_lte', 'tx_log_index_in', 'tx_log_index_not_in')

    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    owner = sgqlc.types.Field(String, graphql_name='owner')
    owner_not = sgqlc.types.Field(String, graphql_name='owner_not')
    owner_gt = sgqlc.types.Field(String, graphql_name='owner_gt')
    owner_lt = sgqlc.types.Field(String, graphql_name='owner_lt')
    owner_gte = sgqlc.types.Field(String, graphql_name='owner_gte')
    owner_lte = sgqlc.types.Field(String, graphql_name='owner_lte')
    owner_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='owner_in')
    owner_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='owner_not_in')
    owner_contains = sgqlc.types.Field(String, graphql_name='owner_contains')
    owner_not_contains = sgqlc.types.Field(String, graphql_name='owner_not_contains')
    owner_starts_with = sgqlc.types.Field(String, graphql_name='owner_starts_with')
    owner_not_starts_with = sgqlc.types.Field(String, graphql_name='owner_not_starts_with')
    owner_ends_with = sgqlc.types.Field(String, graphql_name='owner_ends_with')
    owner_not_ends_with = sgqlc.types.Field(String, graphql_name='owner_not_ends_with')
    order_id = sgqlc.types.Field(Int, graphql_name='orderId')
    order_id_not = sgqlc.types.Field(Int, graphql_name='orderId_not')
    order_id_gt = sgqlc.types.Field(Int, graphql_name='orderId_gt')
    order_id_lt = sgqlc.types.Field(Int, graphql_name='orderId_lt')
    order_id_gte = sgqlc.types.Field(Int, graphql_name='orderId_gte')
    order_id_lte = sgqlc.types.Field(Int, graphql_name='orderId_lte')
    order_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='orderId_in')
    order_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='orderId_not_in')
    from_batch_id = sgqlc.types.Field(BigInt, graphql_name='fromBatchId')
    from_batch_id_not = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_not')
    from_batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_gt')
    from_batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_lt')
    from_batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_gte')
    from_batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_lte')
    from_batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fromBatchId_in')
    from_batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fromBatchId_not_in')
    from_epoch = sgqlc.types.Field(BigInt, graphql_name='fromEpoch')
    from_epoch_not = sgqlc.types.Field(BigInt, graphql_name='fromEpoch_not')
    from_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='fromEpoch_gt')
    from_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='fromEpoch_lt')
    from_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='fromEpoch_gte')
    from_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='fromEpoch_lte')
    from_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fromEpoch_in')
    from_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fromEpoch_not_in')
    until_batch_id = sgqlc.types.Field(BigInt, graphql_name='untilBatchId')
    until_batch_id_not = sgqlc.types.Field(BigInt, graphql_name='untilBatchId_not')
    until_batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='untilBatchId_gt')
    until_batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='untilBatchId_lt')
    until_batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='untilBatchId_gte')
    until_batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='untilBatchId_lte')
    until_batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='untilBatchId_in')
    until_batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='untilBatchId_not_in')
    until_epoch = sgqlc.types.Field(BigInt, graphql_name='untilEpoch')
    until_epoch_not = sgqlc.types.Field(BigInt, graphql_name='untilEpoch_not')
    until_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='untilEpoch_gt')
    until_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='untilEpoch_lt')
    until_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='untilEpoch_gte')
    until_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='untilEpoch_lte')
    until_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='untilEpoch_in')
    until_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='untilEpoch_not_in')
    buy_token = sgqlc.types.Field(String, graphql_name='buyToken')
    buy_token_not = sgqlc.types.Field(String, graphql_name='buyToken_not')
    buy_token_gt = sgqlc.types.Field(String, graphql_name='buyToken_gt')
    buy_token_lt = sgqlc.types.Field(String, graphql_name='buyToken_lt')
    buy_token_gte = sgqlc.types.Field(String, graphql_name='buyToken_gte')
    buy_token_lte = sgqlc.types.Field(String, graphql_name='buyToken_lte')
    buy_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='buyToken_in')
    buy_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='buyToken_not_in')
    buy_token_contains = sgqlc.types.Field(String, graphql_name='buyToken_contains')
    buy_token_not_contains = sgqlc.types.Field(String, graphql_name='buyToken_not_contains')
    buy_token_starts_with = sgqlc.types.Field(String, graphql_name='buyToken_starts_with')
    buy_token_not_starts_with = sgqlc.types.Field(String, graphql_name='buyToken_not_starts_with')
    buy_token_ends_with = sgqlc.types.Field(String, graphql_name='buyToken_ends_with')
    buy_token_not_ends_with = sgqlc.types.Field(String, graphql_name='buyToken_not_ends_with')
    sell_token = sgqlc.types.Field(String, graphql_name='sellToken')
    sell_token_not = sgqlc.types.Field(String, graphql_name='sellToken_not')
    sell_token_gt = sgqlc.types.Field(String, graphql_name='sellToken_gt')
    sell_token_lt = sgqlc.types.Field(String, graphql_name='sellToken_lt')
    sell_token_gte = sgqlc.types.Field(String, graphql_name='sellToken_gte')
    sell_token_lte = sgqlc.types.Field(String, graphql_name='sellToken_lte')
    sell_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sellToken_in')
    sell_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sellToken_not_in')
    sell_token_contains = sgqlc.types.Field(String, graphql_name='sellToken_contains')
    sell_token_not_contains = sgqlc.types.Field(String, graphql_name='sellToken_not_contains')
    sell_token_starts_with = sgqlc.types.Field(String, graphql_name='sellToken_starts_with')
    sell_token_not_starts_with = sgqlc.types.Field(String, graphql_name='sellToken_not_starts_with')
    sell_token_ends_with = sgqlc.types.Field(String, graphql_name='sellToken_ends_with')
    sell_token_not_ends_with = sgqlc.types.Field(String, graphql_name='sellToken_not_ends_with')
    price_numerator = sgqlc.types.Field(BigInt, graphql_name='priceNumerator')
    price_numerator_not = sgqlc.types.Field(BigInt, graphql_name='priceNumerator_not')
    price_numerator_gt = sgqlc.types.Field(BigInt, graphql_name='priceNumerator_gt')
    price_numerator_lt = sgqlc.types.Field(BigInt, graphql_name='priceNumerator_lt')
    price_numerator_gte = sgqlc.types.Field(BigInt, graphql_name='priceNumerator_gte')
    price_numerator_lte = sgqlc.types.Field(BigInt, graphql_name='priceNumerator_lte')
    price_numerator_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='priceNumerator_in')
    price_numerator_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='priceNumerator_not_in')
    price_denominator = sgqlc.types.Field(BigInt, graphql_name='priceDenominator')
    price_denominator_not = sgqlc.types.Field(BigInt, graphql_name='priceDenominator_not')
    price_denominator_gt = sgqlc.types.Field(BigInt, graphql_name='priceDenominator_gt')
    price_denominator_lt = sgqlc.types.Field(BigInt, graphql_name='priceDenominator_lt')
    price_denominator_gte = sgqlc.types.Field(BigInt, graphql_name='priceDenominator_gte')
    price_denominator_lte = sgqlc.types.Field(BigInt, graphql_name='priceDenominator_lte')
    price_denominator_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='priceDenominator_in')
    price_denominator_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='priceDenominator_not_in')
    max_sell_amount = sgqlc.types.Field(BigInt, graphql_name='maxSellAmount')
    max_sell_amount_not = sgqlc.types.Field(BigInt, graphql_name='maxSellAmount_not')
    max_sell_amount_gt = sgqlc.types.Field(BigInt, graphql_name='maxSellAmount_gt')
    max_sell_amount_lt = sgqlc.types.Field(BigInt, graphql_name='maxSellAmount_lt')
    max_sell_amount_gte = sgqlc.types.Field(BigInt, graphql_name='maxSellAmount_gte')
    max_sell_amount_lte = sgqlc.types.Field(BigInt, graphql_name='maxSellAmount_lte')
    max_sell_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='maxSellAmount_in')
    max_sell_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='maxSellAmount_not_in')
    min_receive_amount = sgqlc.types.Field(BigInt, graphql_name='minReceiveAmount')
    min_receive_amount_not = sgqlc.types.Field(BigInt, graphql_name='minReceiveAmount_not')
    min_receive_amount_gt = sgqlc.types.Field(BigInt, graphql_name='minReceiveAmount_gt')
    min_receive_amount_lt = sgqlc.types.Field(BigInt, graphql_name='minReceiveAmount_lt')
    min_receive_amount_gte = sgqlc.types.Field(BigInt, graphql_name='minReceiveAmount_gte')
    min_receive_amount_lte = sgqlc.types.Field(BigInt, graphql_name='minReceiveAmount_lte')
    min_receive_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='minReceiveAmount_in')
    min_receive_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='minReceiveAmount_not_in')
    sold_volume = sgqlc.types.Field(BigInt, graphql_name='soldVolume')
    sold_volume_not = sgqlc.types.Field(BigInt, graphql_name='soldVolume_not')
    sold_volume_gt = sgqlc.types.Field(BigInt, graphql_name='soldVolume_gt')
    sold_volume_lt = sgqlc.types.Field(BigInt, graphql_name='soldVolume_lt')
    sold_volume_gte = sgqlc.types.Field(BigInt, graphql_name='soldVolume_gte')
    sold_volume_lte = sgqlc.types.Field(BigInt, graphql_name='soldVolume_lte')
    sold_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='soldVolume_in')
    sold_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='soldVolume_not_in')
    bought_volume = sgqlc.types.Field(BigInt, graphql_name='boughtVolume')
    bought_volume_not = sgqlc.types.Field(BigInt, graphql_name='boughtVolume_not')
    bought_volume_gt = sgqlc.types.Field(BigInt, graphql_name='boughtVolume_gt')
    bought_volume_lt = sgqlc.types.Field(BigInt, graphql_name='boughtVolume_lt')
    bought_volume_gte = sgqlc.types.Field(BigInt, graphql_name='boughtVolume_gte')
    bought_volume_lte = sgqlc.types.Field(BigInt, graphql_name='boughtVolume_lte')
    bought_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='boughtVolume_in')
    bought_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='boughtVolume_not_in')
    create_epoch = sgqlc.types.Field(BigInt, graphql_name='createEpoch')
    create_epoch_not = sgqlc.types.Field(BigInt, graphql_name='createEpoch_not')
    create_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gt')
    create_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lt')
    create_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gte')
    create_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lte')
    create_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_in')
    create_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_not_in')
    cancel_epoch = sgqlc.types.Field(BigInt, graphql_name='cancelEpoch')
    cancel_epoch_not = sgqlc.types.Field(BigInt, graphql_name='cancelEpoch_not')
    cancel_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='cancelEpoch_gt')
    cancel_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='cancelEpoch_lt')
    cancel_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='cancelEpoch_gte')
    cancel_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='cancelEpoch_lte')
    cancel_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='cancelEpoch_in')
    cancel_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='cancelEpoch_not_in')
    delete_epoch = sgqlc.types.Field(BigInt, graphql_name='deleteEpoch')
    delete_epoch_not = sgqlc.types.Field(BigInt, graphql_name='deleteEpoch_not')
    delete_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='deleteEpoch_gt')
    delete_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='deleteEpoch_lt')
    delete_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='deleteEpoch_gte')
    delete_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='deleteEpoch_lte')
    delete_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='deleteEpoch_in')
    delete_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='deleteEpoch_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')
    tx_log_index = sgqlc.types.Field(BigInt, graphql_name='txLogIndex')
    tx_log_index_not = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_not')
    tx_log_index_gt = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_gt')
    tx_log_index_lt = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_lt')
    tx_log_index_gte = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_gte')
    tx_log_index_lte = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_lte')
    tx_log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txLogIndex_in')
    tx_log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txLogIndex_not_in')


class Price_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_not_contains', 'token_starts_with', 'token_not_starts_with', 'token_ends_with', 'token_not_ends_with', 'batch_id', 'batch_id_not', 'batch_id_gt', 'batch_id_lt', 'batch_id_gte', 'batch_id_lte', 'batch_id_in', 'batch_id_not_in', 'price_in_owl_numerator', 'price_in_owl_numerator_not', 'price_in_owl_numerator_gt', 'price_in_owl_numerator_lt', 'price_in_owl_numerator_gte', 'price_in_owl_numerator_lte', 'price_in_owl_numerator_in', 'price_in_owl_numerator_not_in', 'price_in_owl_denominator', 'price_in_owl_denominator_not', 'price_in_owl_denominator_gt', 'price_in_owl_denominator_lt', 'price_in_owl_denominator_gte', 'price_in_owl_denominator_lte', 'price_in_owl_denominator_in', 'price_in_owl_denominator_not_in', 'volume', 'volume_not', 'volume_gt', 'volume_lt', 'volume_gte', 'volume_lte', 'volume_in', 'volume_not_in', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    token = sgqlc.types.Field(String, graphql_name='token')
    token_not = sgqlc.types.Field(String, graphql_name='token_not')
    token_gt = sgqlc.types.Field(String, graphql_name='token_gt')
    token_lt = sgqlc.types.Field(String, graphql_name='token_lt')
    token_gte = sgqlc.types.Field(String, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(String, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_in')
    token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_not_in')
    token_contains = sgqlc.types.Field(String, graphql_name='token_contains')
    token_not_contains = sgqlc.types.Field(String, graphql_name='token_not_contains')
    token_starts_with = sgqlc.types.Field(String, graphql_name='token_starts_with')
    token_not_starts_with = sgqlc.types.Field(String, graphql_name='token_not_starts_with')
    token_ends_with = sgqlc.types.Field(String, graphql_name='token_ends_with')
    token_not_ends_with = sgqlc.types.Field(String, graphql_name='token_not_ends_with')
    batch_id = sgqlc.types.Field(BigInt, graphql_name='batchId')
    batch_id_not = sgqlc.types.Field(BigInt, graphql_name='batchId_not')
    batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='batchId_gt')
    batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='batchId_lt')
    batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='batchId_gte')
    batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='batchId_lte')
    batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='batchId_in')
    batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='batchId_not_in')
    price_in_owl_numerator = sgqlc.types.Field(BigInt, graphql_name='priceInOwlNumerator')
    price_in_owl_numerator_not = sgqlc.types.Field(BigInt, graphql_name='priceInOwlNumerator_not')
    price_in_owl_numerator_gt = sgqlc.types.Field(BigInt, graphql_name='priceInOwlNumerator_gt')
    price_in_owl_numerator_lt = sgqlc.types.Field(BigInt, graphql_name='priceInOwlNumerator_lt')
    price_in_owl_numerator_gte = sgqlc.types.Field(BigInt, graphql_name='priceInOwlNumerator_gte')
    price_in_owl_numerator_lte = sgqlc.types.Field(BigInt, graphql_name='priceInOwlNumerator_lte')
    price_in_owl_numerator_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='priceInOwlNumerator_in')
    price_in_owl_numerator_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='priceInOwlNumerator_not_in')
    price_in_owl_denominator = sgqlc.types.Field(BigInt, graphql_name='priceInOwlDenominator')
    price_in_owl_denominator_not = sgqlc.types.Field(BigInt, graphql_name='priceInOwlDenominator_not')
    price_in_owl_denominator_gt = sgqlc.types.Field(BigInt, graphql_name='priceInOwlDenominator_gt')
    price_in_owl_denominator_lt = sgqlc.types.Field(BigInt, graphql_name='priceInOwlDenominator_lt')
    price_in_owl_denominator_gte = sgqlc.types.Field(BigInt, graphql_name='priceInOwlDenominator_gte')
    price_in_owl_denominator_lte = sgqlc.types.Field(BigInt, graphql_name='priceInOwlDenominator_lte')
    price_in_owl_denominator_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='priceInOwlDenominator_in')
    price_in_owl_denominator_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='priceInOwlDenominator_not_in')
    volume = sgqlc.types.Field(BigInt, graphql_name='volume')
    volume_not = sgqlc.types.Field(BigInt, graphql_name='volume_not')
    volume_gt = sgqlc.types.Field(BigInt, graphql_name='volume_gt')
    volume_lt = sgqlc.types.Field(BigInt, graphql_name='volume_lt')
    volume_gte = sgqlc.types.Field(BigInt, graphql_name='volume_gte')
    volume_lte = sgqlc.types.Field(BigInt, graphql_name='volume_lte')
    volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='volume_in')
    volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='volume_not_in')
    create_epoch = sgqlc.types.Field(BigInt, graphql_name='createEpoch')
    create_epoch_not = sgqlc.types.Field(BigInt, graphql_name='createEpoch_not')
    create_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gt')
    create_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lt')
    create_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gte')
    create_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lte')
    create_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_in')
    create_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')


class Solution_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'batch', 'batch_not', 'batch_gt', 'batch_lt', 'batch_gte', 'batch_lte', 'batch_in', 'batch_not_in', 'batch_contains', 'batch_not_contains', 'batch_starts_with', 'batch_not_starts_with', 'batch_ends_with', 'batch_not_ends_with', 'solver', 'solver_not', 'solver_gt', 'solver_lt', 'solver_gte', 'solver_lte', 'solver_in', 'solver_not_in', 'solver_contains', 'solver_not_contains', 'solver_starts_with', 'solver_not_starts_with', 'solver_ends_with', 'solver_not_ends_with', 'fee_reward', 'fee_reward_not', 'fee_reward_gt', 'fee_reward_lt', 'fee_reward_gte', 'fee_reward_lte', 'fee_reward_in', 'fee_reward_not_in', 'objective_value', 'objective_value_not', 'objective_value_gt', 'objective_value_lt', 'objective_value_gte', 'objective_value_lte', 'objective_value_in', 'objective_value_not_in', 'trades', 'trades_not', 'trades_contains', 'trades_not_contains', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'revert_epoch', 'revert_epoch_not', 'revert_epoch_gt', 'revert_epoch_lt', 'revert_epoch_gte', 'revert_epoch_lte', 'revert_epoch_in', 'revert_epoch_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains', 'tx_log_index', 'tx_log_index_not', 'tx_log_index_gt', 'tx_log_index_lt', 'tx_log_index_gte', 'tx_log_index_lte', 'tx_log_index_in', 'tx_log_index_not_in')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    batch = sgqlc.types.Field(String, graphql_name='batch')
    batch_not = sgqlc.types.Field(String, graphql_name='batch_not')
    batch_gt = sgqlc.types.Field(String, graphql_name='batch_gt')
    batch_lt = sgqlc.types.Field(String, graphql_name='batch_lt')
    batch_gte = sgqlc.types.Field(String, graphql_name='batch_gte')
    batch_lte = sgqlc.types.Field(String, graphql_name='batch_lte')
    batch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='batch_in')
    batch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='batch_not_in')
    batch_contains = sgqlc.types.Field(String, graphql_name='batch_contains')
    batch_not_contains = sgqlc.types.Field(String, graphql_name='batch_not_contains')
    batch_starts_with = sgqlc.types.Field(String, graphql_name='batch_starts_with')
    batch_not_starts_with = sgqlc.types.Field(String, graphql_name='batch_not_starts_with')
    batch_ends_with = sgqlc.types.Field(String, graphql_name='batch_ends_with')
    batch_not_ends_with = sgqlc.types.Field(String, graphql_name='batch_not_ends_with')
    solver = sgqlc.types.Field(String, graphql_name='solver')
    solver_not = sgqlc.types.Field(String, graphql_name='solver_not')
    solver_gt = sgqlc.types.Field(String, graphql_name='solver_gt')
    solver_lt = sgqlc.types.Field(String, graphql_name='solver_lt')
    solver_gte = sgqlc.types.Field(String, graphql_name='solver_gte')
    solver_lte = sgqlc.types.Field(String, graphql_name='solver_lte')
    solver_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='solver_in')
    solver_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='solver_not_in')
    solver_contains = sgqlc.types.Field(String, graphql_name='solver_contains')
    solver_not_contains = sgqlc.types.Field(String, graphql_name='solver_not_contains')
    solver_starts_with = sgqlc.types.Field(String, graphql_name='solver_starts_with')
    solver_not_starts_with = sgqlc.types.Field(String, graphql_name='solver_not_starts_with')
    solver_ends_with = sgqlc.types.Field(String, graphql_name='solver_ends_with')
    solver_not_ends_with = sgqlc.types.Field(String, graphql_name='solver_not_ends_with')
    fee_reward = sgqlc.types.Field(BigInt, graphql_name='feeReward')
    fee_reward_not = sgqlc.types.Field(BigInt, graphql_name='feeReward_not')
    fee_reward_gt = sgqlc.types.Field(BigInt, graphql_name='feeReward_gt')
    fee_reward_lt = sgqlc.types.Field(BigInt, graphql_name='feeReward_lt')
    fee_reward_gte = sgqlc.types.Field(BigInt, graphql_name='feeReward_gte')
    fee_reward_lte = sgqlc.types.Field(BigInt, graphql_name='feeReward_lte')
    fee_reward_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='feeReward_in')
    fee_reward_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='feeReward_not_in')
    objective_value = sgqlc.types.Field(BigInt, graphql_name='objectiveValue')
    objective_value_not = sgqlc.types.Field(BigInt, graphql_name='objectiveValue_not')
    objective_value_gt = sgqlc.types.Field(BigInt, graphql_name='objectiveValue_gt')
    objective_value_lt = sgqlc.types.Field(BigInt, graphql_name='objectiveValue_lt')
    objective_value_gte = sgqlc.types.Field(BigInt, graphql_name='objectiveValue_gte')
    objective_value_lte = sgqlc.types.Field(BigInt, graphql_name='objectiveValue_lte')
    objective_value_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='objectiveValue_in')
    objective_value_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='objectiveValue_not_in')
    trades = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='trades')
    trades_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='trades_not')
    trades_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='trades_contains')
    trades_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='trades_not_contains')
    create_epoch = sgqlc.types.Field(BigInt, graphql_name='createEpoch')
    create_epoch_not = sgqlc.types.Field(BigInt, graphql_name='createEpoch_not')
    create_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gt')
    create_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lt')
    create_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gte')
    create_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lte')
    create_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_in')
    create_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_not_in')
    revert_epoch = sgqlc.types.Field(BigInt, graphql_name='revertEpoch')
    revert_epoch_not = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_not')
    revert_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_gt')
    revert_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_lt')
    revert_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_gte')
    revert_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_lte')
    revert_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='revertEpoch_in')
    revert_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='revertEpoch_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')
    tx_log_index = sgqlc.types.Field(BigInt, graphql_name='txLogIndex')
    tx_log_index_not = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_not')
    tx_log_index_gt = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_gt')
    tx_log_index_lt = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_lt')
    tx_log_index_gte = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_gte')
    tx_log_index_lte = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_lte')
    tx_log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txLogIndex_in')
    tx_log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txLogIndex_not_in')


class Token_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'address', 'address_not', 'address_in', 'address_not_in', 'address_contains', 'address_not_contains', 'from_batch_id', 'from_batch_id_not', 'from_batch_id_gt', 'from_batch_id_lt', 'from_batch_id_gte', 'from_batch_id_lte', 'from_batch_id_in', 'from_batch_id_not_in', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_not_contains', 'symbol_starts_with', 'symbol_not_starts_with', 'symbol_ends_with', 'symbol_not_ends_with', 'decimals', 'decimals_not', 'decimals_gt', 'decimals_lt', 'decimals_gte', 'decimals_lte', 'decimals_in', 'decimals_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_not_contains', 'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    address = sgqlc.types.Field(Bytes, graphql_name='address')
    address_not = sgqlc.types.Field(Bytes, graphql_name='address_not')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(Bytes, graphql_name='address_contains')
    address_not_contains = sgqlc.types.Field(Bytes, graphql_name='address_not_contains')
    from_batch_id = sgqlc.types.Field(BigInt, graphql_name='fromBatchId')
    from_batch_id_not = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_not')
    from_batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_gt')
    from_batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_lt')
    from_batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_gte')
    from_batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_lte')
    from_batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fromBatchId_in')
    from_batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fromBatchId_not_in')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    symbol_not = sgqlc.types.Field(String, graphql_name='symbol_not')
    symbol_gt = sgqlc.types.Field(String, graphql_name='symbol_gt')
    symbol_lt = sgqlc.types.Field(String, graphql_name='symbol_lt')
    symbol_gte = sgqlc.types.Field(String, graphql_name='symbol_gte')
    symbol_lte = sgqlc.types.Field(String, graphql_name='symbol_lte')
    symbol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_in')
    symbol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_not_in')
    symbol_contains = sgqlc.types.Field(String, graphql_name='symbol_contains')
    symbol_not_contains = sgqlc.types.Field(String, graphql_name='symbol_not_contains')
    symbol_starts_with = sgqlc.types.Field(String, graphql_name='symbol_starts_with')
    symbol_not_starts_with = sgqlc.types.Field(String, graphql_name='symbol_not_starts_with')
    symbol_ends_with = sgqlc.types.Field(String, graphql_name='symbol_ends_with')
    symbol_not_ends_with = sgqlc.types.Field(String, graphql_name='symbol_not_ends_with')
    decimals = sgqlc.types.Field(BigInt, graphql_name='decimals')
    decimals_not = sgqlc.types.Field(BigInt, graphql_name='decimals_not')
    decimals_gt = sgqlc.types.Field(BigInt, graphql_name='decimals_gt')
    decimals_lt = sgqlc.types.Field(BigInt, graphql_name='decimals_lt')
    decimals_gte = sgqlc.types.Field(BigInt, graphql_name='decimals_gte')
    decimals_lte = sgqlc.types.Field(BigInt, graphql_name='decimals_lte')
    decimals_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='decimals_in')
    decimals_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='decimals_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    create_epoch = sgqlc.types.Field(BigInt, graphql_name='createEpoch')
    create_epoch_not = sgqlc.types.Field(BigInt, graphql_name='createEpoch_not')
    create_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gt')
    create_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lt')
    create_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gte')
    create_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lte')
    create_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_in')
    create_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')


class Trade_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'order', 'order_not', 'order_gt', 'order_lt', 'order_gte', 'order_lte', 'order_in', 'order_not_in', 'order_contains', 'order_not_contains', 'order_starts_with', 'order_not_starts_with', 'order_ends_with', 'order_not_ends_with', 'owner', 'owner_not', 'owner_gt', 'owner_lt', 'owner_gte', 'owner_lte', 'owner_in', 'owner_not_in', 'owner_contains', 'owner_not_contains', 'owner_starts_with', 'owner_not_starts_with', 'owner_ends_with', 'owner_not_ends_with', 'sell_volume', 'sell_volume_not', 'sell_volume_gt', 'sell_volume_lt', 'sell_volume_gte', 'sell_volume_lte', 'sell_volume_in', 'sell_volume_not_in', 'buy_volume', 'buy_volume_not', 'buy_volume_gt', 'buy_volume_lt', 'buy_volume_gte', 'buy_volume_lte', 'buy_volume_in', 'buy_volume_not_in', 'trade_batch_id', 'trade_batch_id_not', 'trade_batch_id_gt', 'trade_batch_id_lt', 'trade_batch_id_gte', 'trade_batch_id_lte', 'trade_batch_id_in', 'trade_batch_id_not_in', 'trade_epoch', 'trade_epoch_not', 'trade_epoch_gt', 'trade_epoch_lt', 'trade_epoch_gte', 'trade_epoch_lte', 'trade_epoch_in', 'trade_epoch_not_in', 'buy_token', 'buy_token_not', 'buy_token_gt', 'buy_token_lt', 'buy_token_gte', 'buy_token_lte', 'buy_token_in', 'buy_token_not_in', 'buy_token_contains', 'buy_token_not_contains', 'buy_token_starts_with', 'buy_token_not_starts_with', 'buy_token_ends_with', 'buy_token_not_ends_with', 'sell_token', 'sell_token_not', 'sell_token_gt', 'sell_token_lt', 'sell_token_gte', 'sell_token_lte', 'sell_token_in', 'sell_token_not_in', 'sell_token_contains', 'sell_token_not_contains', 'sell_token_starts_with', 'sell_token_not_starts_with', 'sell_token_ends_with', 'sell_token_not_ends_with', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'revert_epoch', 'revert_epoch_not', 'revert_epoch_gt', 'revert_epoch_lt', 'revert_epoch_gte', 'revert_epoch_lte', 'revert_epoch_in', 'revert_epoch_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains', 'tx_log_index', 'tx_log_index_not', 'tx_log_index_gt', 'tx_log_index_lt', 'tx_log_index_gte', 'tx_log_index_lte', 'tx_log_index_in', 'tx_log_index_not_in')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    order = sgqlc.types.Field(String, graphql_name='order')
    order_not = sgqlc.types.Field(String, graphql_name='order_not')
    order_gt = sgqlc.types.Field(String, graphql_name='order_gt')
    order_lt = sgqlc.types.Field(String, graphql_name='order_lt')
    order_gte = sgqlc.types.Field(String, graphql_name='order_gte')
    order_lte = sgqlc.types.Field(String, graphql_name='order_lte')
    order_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='order_in')
    order_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='order_not_in')
    order_contains = sgqlc.types.Field(String, graphql_name='order_contains')
    order_not_contains = sgqlc.types.Field(String, graphql_name='order_not_contains')
    order_starts_with = sgqlc.types.Field(String, graphql_name='order_starts_with')
    order_not_starts_with = sgqlc.types.Field(String, graphql_name='order_not_starts_with')
    order_ends_with = sgqlc.types.Field(String, graphql_name='order_ends_with')
    order_not_ends_with = sgqlc.types.Field(String, graphql_name='order_not_ends_with')
    owner = sgqlc.types.Field(String, graphql_name='owner')
    owner_not = sgqlc.types.Field(String, graphql_name='owner_not')
    owner_gt = sgqlc.types.Field(String, graphql_name='owner_gt')
    owner_lt = sgqlc.types.Field(String, graphql_name='owner_lt')
    owner_gte = sgqlc.types.Field(String, graphql_name='owner_gte')
    owner_lte = sgqlc.types.Field(String, graphql_name='owner_lte')
    owner_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='owner_in')
    owner_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='owner_not_in')
    owner_contains = sgqlc.types.Field(String, graphql_name='owner_contains')
    owner_not_contains = sgqlc.types.Field(String, graphql_name='owner_not_contains')
    owner_starts_with = sgqlc.types.Field(String, graphql_name='owner_starts_with')
    owner_not_starts_with = sgqlc.types.Field(String, graphql_name='owner_not_starts_with')
    owner_ends_with = sgqlc.types.Field(String, graphql_name='owner_ends_with')
    owner_not_ends_with = sgqlc.types.Field(String, graphql_name='owner_not_ends_with')
    sell_volume = sgqlc.types.Field(BigInt, graphql_name='sellVolume')
    sell_volume_not = sgqlc.types.Field(BigInt, graphql_name='sellVolume_not')
    sell_volume_gt = sgqlc.types.Field(BigInt, graphql_name='sellVolume_gt')
    sell_volume_lt = sgqlc.types.Field(BigInt, graphql_name='sellVolume_lt')
    sell_volume_gte = sgqlc.types.Field(BigInt, graphql_name='sellVolume_gte')
    sell_volume_lte = sgqlc.types.Field(BigInt, graphql_name='sellVolume_lte')
    sell_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sellVolume_in')
    sell_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sellVolume_not_in')
    buy_volume = sgqlc.types.Field(BigInt, graphql_name='buyVolume')
    buy_volume_not = sgqlc.types.Field(BigInt, graphql_name='buyVolume_not')
    buy_volume_gt = sgqlc.types.Field(BigInt, graphql_name='buyVolume_gt')
    buy_volume_lt = sgqlc.types.Field(BigInt, graphql_name='buyVolume_lt')
    buy_volume_gte = sgqlc.types.Field(BigInt, graphql_name='buyVolume_gte')
    buy_volume_lte = sgqlc.types.Field(BigInt, graphql_name='buyVolume_lte')
    buy_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='buyVolume_in')
    buy_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='buyVolume_not_in')
    trade_batch_id = sgqlc.types.Field(BigInt, graphql_name='tradeBatchId')
    trade_batch_id_not = sgqlc.types.Field(BigInt, graphql_name='tradeBatchId_not')
    trade_batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='tradeBatchId_gt')
    trade_batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='tradeBatchId_lt')
    trade_batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='tradeBatchId_gte')
    trade_batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='tradeBatchId_lte')
    trade_batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tradeBatchId_in')
    trade_batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tradeBatchId_not_in')
    trade_epoch = sgqlc.types.Field(BigInt, graphql_name='tradeEpoch')
    trade_epoch_not = sgqlc.types.Field(BigInt, graphql_name='tradeEpoch_not')
    trade_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='tradeEpoch_gt')
    trade_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='tradeEpoch_lt')
    trade_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='tradeEpoch_gte')
    trade_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='tradeEpoch_lte')
    trade_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tradeEpoch_in')
    trade_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tradeEpoch_not_in')
    buy_token = sgqlc.types.Field(String, graphql_name='buyToken')
    buy_token_not = sgqlc.types.Field(String, graphql_name='buyToken_not')
    buy_token_gt = sgqlc.types.Field(String, graphql_name='buyToken_gt')
    buy_token_lt = sgqlc.types.Field(String, graphql_name='buyToken_lt')
    buy_token_gte = sgqlc.types.Field(String, graphql_name='buyToken_gte')
    buy_token_lte = sgqlc.types.Field(String, graphql_name='buyToken_lte')
    buy_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='buyToken_in')
    buy_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='buyToken_not_in')
    buy_token_contains = sgqlc.types.Field(String, graphql_name='buyToken_contains')
    buy_token_not_contains = sgqlc.types.Field(String, graphql_name='buyToken_not_contains')
    buy_token_starts_with = sgqlc.types.Field(String, graphql_name='buyToken_starts_with')
    buy_token_not_starts_with = sgqlc.types.Field(String, graphql_name='buyToken_not_starts_with')
    buy_token_ends_with = sgqlc.types.Field(String, graphql_name='buyToken_ends_with')
    buy_token_not_ends_with = sgqlc.types.Field(String, graphql_name='buyToken_not_ends_with')
    sell_token = sgqlc.types.Field(String, graphql_name='sellToken')
    sell_token_not = sgqlc.types.Field(String, graphql_name='sellToken_not')
    sell_token_gt = sgqlc.types.Field(String, graphql_name='sellToken_gt')
    sell_token_lt = sgqlc.types.Field(String, graphql_name='sellToken_lt')
    sell_token_gte = sgqlc.types.Field(String, graphql_name='sellToken_gte')
    sell_token_lte = sgqlc.types.Field(String, graphql_name='sellToken_lte')
    sell_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sellToken_in')
    sell_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sellToken_not_in')
    sell_token_contains = sgqlc.types.Field(String, graphql_name='sellToken_contains')
    sell_token_not_contains = sgqlc.types.Field(String, graphql_name='sellToken_not_contains')
    sell_token_starts_with = sgqlc.types.Field(String, graphql_name='sellToken_starts_with')
    sell_token_not_starts_with = sgqlc.types.Field(String, graphql_name='sellToken_not_starts_with')
    sell_token_ends_with = sgqlc.types.Field(String, graphql_name='sellToken_ends_with')
    sell_token_not_ends_with = sgqlc.types.Field(String, graphql_name='sellToken_not_ends_with')
    create_epoch = sgqlc.types.Field(BigInt, graphql_name='createEpoch')
    create_epoch_not = sgqlc.types.Field(BigInt, graphql_name='createEpoch_not')
    create_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gt')
    create_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lt')
    create_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gte')
    create_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lte')
    create_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_in')
    create_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_not_in')
    revert_epoch = sgqlc.types.Field(BigInt, graphql_name='revertEpoch')
    revert_epoch_not = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_not')
    revert_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_gt')
    revert_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_lt')
    revert_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_gte')
    revert_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='revertEpoch_lte')
    revert_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='revertEpoch_in')
    revert_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='revertEpoch_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')
    tx_log_index = sgqlc.types.Field(BigInt, graphql_name='txLogIndex')
    tx_log_index_not = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_not')
    tx_log_index_gt = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_gt')
    tx_log_index_lt = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_lt')
    tx_log_index_gte = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_gte')
    tx_log_index_lte = sgqlc.types.Field(BigInt, graphql_name='txLogIndex_lte')
    tx_log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txLogIndex_in')
    tx_log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txLogIndex_not_in')


class User_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'from_batch_id', 'from_batch_id_not', 'from_batch_id_gt', 'from_batch_id_lt', 'from_batch_id_gte', 'from_batch_id_lte', 'from_batch_id_in', 'from_batch_id_not_in', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    from_batch_id = sgqlc.types.Field(BigInt, graphql_name='fromBatchId')
    from_batch_id_not = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_not')
    from_batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_gt')
    from_batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_lt')
    from_batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_gte')
    from_batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='fromBatchId_lte')
    from_batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fromBatchId_in')
    from_batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fromBatchId_not_in')
    create_epoch = sgqlc.types.Field(BigInt, graphql_name='createEpoch')
    create_epoch_not = sgqlc.types.Field(BigInt, graphql_name='createEpoch_not')
    create_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gt')
    create_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lt')
    create_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gte')
    create_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lte')
    create_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_in')
    create_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')


class WithdrawRequest_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'user', 'user_not', 'user_gt', 'user_lt', 'user_gte', 'user_lte', 'user_in', 'user_not_in', 'user_contains', 'user_not_contains', 'user_starts_with', 'user_not_starts_with', 'user_ends_with', 'user_not_ends_with', 'token_address', 'token_address_not', 'token_address_in', 'token_address_not_in', 'token_address_contains', 'token_address_not_contains', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'withdrawable_from_batch_id', 'withdrawable_from_batch_id_not', 'withdrawable_from_batch_id_gt', 'withdrawable_from_batch_id_lt', 'withdrawable_from_batch_id_gte', 'withdrawable_from_batch_id_lte', 'withdrawable_from_batch_id_in', 'withdrawable_from_batch_id_not_in', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'create_batch_id', 'create_batch_id_not', 'create_batch_id_gt', 'create_batch_id_lt', 'create_batch_id_gte', 'create_batch_id_lte', 'create_batch_id_in', 'create_batch_id_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    user = sgqlc.types.Field(String, graphql_name='user')
    user_not = sgqlc.types.Field(String, graphql_name='user_not')
    user_gt = sgqlc.types.Field(String, graphql_name='user_gt')
    user_lt = sgqlc.types.Field(String, graphql_name='user_lt')
    user_gte = sgqlc.types.Field(String, graphql_name='user_gte')
    user_lte = sgqlc.types.Field(String, graphql_name='user_lte')
    user_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_in')
    user_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_not_in')
    user_contains = sgqlc.types.Field(String, graphql_name='user_contains')
    user_not_contains = sgqlc.types.Field(String, graphql_name='user_not_contains')
    user_starts_with = sgqlc.types.Field(String, graphql_name='user_starts_with')
    user_not_starts_with = sgqlc.types.Field(String, graphql_name='user_not_starts_with')
    user_ends_with = sgqlc.types.Field(String, graphql_name='user_ends_with')
    user_not_ends_with = sgqlc.types.Field(String, graphql_name='user_not_ends_with')
    token_address = sgqlc.types.Field(Bytes, graphql_name='tokenAddress')
    token_address_not = sgqlc.types.Field(Bytes, graphql_name='tokenAddress_not')
    token_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenAddress_in')
    token_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenAddress_not_in')
    token_address_contains = sgqlc.types.Field(Bytes, graphql_name='tokenAddress_contains')
    token_address_not_contains = sgqlc.types.Field(Bytes, graphql_name='tokenAddress_not_contains')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigInt, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigInt, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigInt, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigInt, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigInt, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_not_in')
    withdrawable_from_batch_id = sgqlc.types.Field(BigInt, graphql_name='withdrawableFromBatchId')
    withdrawable_from_batch_id_not = sgqlc.types.Field(BigInt, graphql_name='withdrawableFromBatchId_not')
    withdrawable_from_batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='withdrawableFromBatchId_gt')
    withdrawable_from_batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='withdrawableFromBatchId_lt')
    withdrawable_from_batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='withdrawableFromBatchId_gte')
    withdrawable_from_batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='withdrawableFromBatchId_lte')
    withdrawable_from_batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='withdrawableFromBatchId_in')
    withdrawable_from_batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='withdrawableFromBatchId_not_in')
    create_epoch = sgqlc.types.Field(BigInt, graphql_name='createEpoch')
    create_epoch_not = sgqlc.types.Field(BigInt, graphql_name='createEpoch_not')
    create_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gt')
    create_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lt')
    create_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gte')
    create_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lte')
    create_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_in')
    create_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_not_in')
    create_batch_id = sgqlc.types.Field(BigInt, graphql_name='createBatchId')
    create_batch_id_not = sgqlc.types.Field(BigInt, graphql_name='createBatchId_not')
    create_batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='createBatchId_gt')
    create_batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='createBatchId_lt')
    create_batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='createBatchId_gte')
    create_batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='createBatchId_lte')
    create_batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createBatchId_in')
    create_batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createBatchId_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')


class Withdraw_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'user', 'user_not', 'user_gt', 'user_lt', 'user_gte', 'user_lte', 'user_in', 'user_not_in', 'user_contains', 'user_not_contains', 'user_starts_with', 'user_not_starts_with', 'user_ends_with', 'user_not_ends_with', 'token_address', 'token_address_not', 'token_address_in', 'token_address_not_in', 'token_address_contains', 'token_address_not_contains', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'create_epoch', 'create_epoch_not', 'create_epoch_gt', 'create_epoch_lt', 'create_epoch_gte', 'create_epoch_lte', 'create_epoch_in', 'create_epoch_not_in', 'create_batch_id', 'create_batch_id_not', 'create_batch_id_gt', 'create_batch_id_lt', 'create_batch_id_gte', 'create_batch_id_lte', 'create_batch_id_in', 'create_batch_id_not_in', 'tx_hash', 'tx_hash_not', 'tx_hash_in', 'tx_hash_not_in', 'tx_hash_contains', 'tx_hash_not_contains')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    user = sgqlc.types.Field(String, graphql_name='user')
    user_not = sgqlc.types.Field(String, graphql_name='user_not')
    user_gt = sgqlc.types.Field(String, graphql_name='user_gt')
    user_lt = sgqlc.types.Field(String, graphql_name='user_lt')
    user_gte = sgqlc.types.Field(String, graphql_name='user_gte')
    user_lte = sgqlc.types.Field(String, graphql_name='user_lte')
    user_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_in')
    user_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_not_in')
    user_contains = sgqlc.types.Field(String, graphql_name='user_contains')
    user_not_contains = sgqlc.types.Field(String, graphql_name='user_not_contains')
    user_starts_with = sgqlc.types.Field(String, graphql_name='user_starts_with')
    user_not_starts_with = sgqlc.types.Field(String, graphql_name='user_not_starts_with')
    user_ends_with = sgqlc.types.Field(String, graphql_name='user_ends_with')
    user_not_ends_with = sgqlc.types.Field(String, graphql_name='user_not_ends_with')
    token_address = sgqlc.types.Field(Bytes, graphql_name='tokenAddress')
    token_address_not = sgqlc.types.Field(Bytes, graphql_name='tokenAddress_not')
    token_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenAddress_in')
    token_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenAddress_not_in')
    token_address_contains = sgqlc.types.Field(Bytes, graphql_name='tokenAddress_contains')
    token_address_not_contains = sgqlc.types.Field(Bytes, graphql_name='tokenAddress_not_contains')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigInt, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigInt, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigInt, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigInt, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigInt, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_not_in')
    create_epoch = sgqlc.types.Field(BigInt, graphql_name='createEpoch')
    create_epoch_not = sgqlc.types.Field(BigInt, graphql_name='createEpoch_not')
    create_epoch_gt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gt')
    create_epoch_lt = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lt')
    create_epoch_gte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_gte')
    create_epoch_lte = sgqlc.types.Field(BigInt, graphql_name='createEpoch_lte')
    create_epoch_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_in')
    create_epoch_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createEpoch_not_in')
    create_batch_id = sgqlc.types.Field(BigInt, graphql_name='createBatchId')
    create_batch_id_not = sgqlc.types.Field(BigInt, graphql_name='createBatchId_not')
    create_batch_id_gt = sgqlc.types.Field(BigInt, graphql_name='createBatchId_gt')
    create_batch_id_lt = sgqlc.types.Field(BigInt, graphql_name='createBatchId_lt')
    create_batch_id_gte = sgqlc.types.Field(BigInt, graphql_name='createBatchId_gte')
    create_batch_id_lte = sgqlc.types.Field(BigInt, graphql_name='createBatchId_lte')
    create_batch_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createBatchId_in')
    create_batch_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createBatchId_not_in')
    tx_hash = sgqlc.types.Field(Bytes, graphql_name='txHash')
    tx_hash_not = sgqlc.types.Field(Bytes, graphql_name='txHash_not')
    tx_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_in')
    tx_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txHash_not_in')
    tx_hash_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_contains')
    tx_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='txHash_not_contains')



########################################################################
# Output Objects and Interfaces
########################################################################
class Batch(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'start_epoch', 'end_epoch', 'solution', 'solutions', 'first_solution_epoch', 'last_revert_epoch', 'tx_hash')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    start_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='startEpoch')
    end_epoch = sgqlc.types.Field(BigInt, graphql_name='endEpoch')
    solution = sgqlc.types.Field(sgqlc.types.non_null('Solution'), graphql_name='solution')
    solutions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Solution'))), graphql_name='solutions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Solution_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Solution_filter, graphql_name='where', default=None)),
))
    )
    first_solution_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='firstSolutionEpoch')
    last_revert_epoch = sgqlc.types.Field(BigInt, graphql_name='lastRevertEpoch')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')


class Deposit(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'user', 'token_address', 'amount', 'batch_id', 'create_epoch', 'tx_hash')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    token_address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='tokenAddress')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='batchId')
    create_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createEpoch')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')


class Order(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'owner', 'order_id', 'from_batch_id', 'from_epoch', 'until_batch_id', 'until_epoch', 'buy_token', 'sell_token', 'price_numerator', 'price_denominator', 'max_sell_amount', 'min_receive_amount', 'sold_volume', 'bought_volume', 'trades', 'create_epoch', 'cancel_epoch', 'delete_epoch', 'tx_hash', 'tx_log_index')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    owner = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='owner')
    order_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='orderId')
    from_batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='fromBatchId')
    from_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='fromEpoch')
    until_batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='untilBatchId')
    until_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='untilEpoch')
    buy_token = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='buyToken')
    sell_token = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='sellToken')
    price_numerator = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='priceNumerator')
    price_denominator = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='priceDenominator')
    max_sell_amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='maxSellAmount')
    min_receive_amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='minReceiveAmount')
    sold_volume = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='soldVolume')
    bought_volume = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='boughtVolume')
    trades = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Trade'))), graphql_name='trades', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Trade_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Trade_filter, graphql_name='where', default=None)),
))
    )
    create_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createEpoch')
    cancel_epoch = sgqlc.types.Field(BigInt, graphql_name='cancelEpoch')
    delete_epoch = sgqlc.types.Field(BigInt, graphql_name='deleteEpoch')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')
    tx_log_index = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='txLogIndex')


class Price(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'token', 'batch_id', 'price_in_owl_numerator', 'price_in_owl_denominator', 'volume', 'create_epoch', 'tx_hash')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    token = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token')
    batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='batchId')
    price_in_owl_numerator = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='priceInOwlNumerator')
    price_in_owl_denominator = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='priceInOwlDenominator')
    volume = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='volume')
    create_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createEpoch')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')


class Query(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('token', 'tokens', 'price', 'prices', 'user', 'users', 'deposit', 'deposits', 'withdraw_request', 'withdraw_requests', 'withdraw', 'withdraws', 'order', 'orders', 'trade', 'trades', 'batch', 'batches', 'solution', 'solutions')
    token = sgqlc.types.Field('Token', graphql_name='token', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='tokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    price = sgqlc.types.Field(Price, graphql_name='price', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    prices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Price))), graphql_name='prices', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Price_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Price_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='users', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(User_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(User_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    deposit = sgqlc.types.Field(Deposit, graphql_name='deposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Deposit))), graphql_name='deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Deposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Deposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    withdraw_request = sgqlc.types.Field('WithdrawRequest', graphql_name='withdrawRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    withdraw_requests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WithdrawRequest'))), graphql_name='withdrawRequests', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(WithdrawRequest_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(WithdrawRequest_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    withdraw = sgqlc.types.Field('Withdraw', graphql_name='withdraw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Withdraw'))), graphql_name='withdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Withdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Withdraw_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    order = sgqlc.types.Field(Order, graphql_name='order', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    orders = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Order))), graphql_name='orders', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Order_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Order_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    trade = sgqlc.types.Field('Trade', graphql_name='trade', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    trades = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Trade'))), graphql_name='trades', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Trade_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Trade_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    batch = sgqlc.types.Field(Batch, graphql_name='batch', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    batches = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Batch))), graphql_name='batches', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Batch_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Batch_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    solution = sgqlc.types.Field('Solution', graphql_name='solution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    solutions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Solution'))), graphql_name='solutions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Solution_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Solution_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class Solution(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'batch', 'solver', 'fee_reward', 'objective_value', 'trades', 'create_epoch', 'revert_epoch', 'tx_hash', 'tx_log_index')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    batch = sgqlc.types.Field(sgqlc.types.non_null(Batch), graphql_name='batch')
    solver = sgqlc.types.Field('User', graphql_name='solver')
    fee_reward = sgqlc.types.Field(BigInt, graphql_name='feeReward')
    objective_value = sgqlc.types.Field(BigInt, graphql_name='objectiveValue')
    trades = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Trade'))), graphql_name='trades', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Trade_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Trade_filter, graphql_name='where', default=None)),
))
    )
    create_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createEpoch')
    revert_epoch = sgqlc.types.Field(BigInt, graphql_name='revertEpoch')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')
    tx_log_index = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='txLogIndex')


class Subscription(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('token', 'tokens', 'price', 'prices', 'user', 'users', 'deposit', 'deposits', 'withdraw_request', 'withdraw_requests', 'withdraw', 'withdraws', 'order', 'orders', 'trade', 'trades', 'batch', 'batches', 'solution', 'solutions')
    token = sgqlc.types.Field('Token', graphql_name='token', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='tokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    price = sgqlc.types.Field(Price, graphql_name='price', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    prices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Price))), graphql_name='prices', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Price_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Price_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='users', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(User_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(User_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    deposit = sgqlc.types.Field(Deposit, graphql_name='deposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Deposit))), graphql_name='deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Deposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Deposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    withdraw_request = sgqlc.types.Field('WithdrawRequest', graphql_name='withdrawRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    withdraw_requests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WithdrawRequest'))), graphql_name='withdrawRequests', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(WithdrawRequest_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(WithdrawRequest_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    withdraw = sgqlc.types.Field('Withdraw', graphql_name='withdraw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Withdraw'))), graphql_name='withdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Withdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Withdraw_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    order = sgqlc.types.Field(Order, graphql_name='order', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    orders = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Order))), graphql_name='orders', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Order_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Order_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    trade = sgqlc.types.Field('Trade', graphql_name='trade', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    trades = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Trade'))), graphql_name='trades', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Trade_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Trade_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    batch = sgqlc.types.Field(Batch, graphql_name='batch', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    batches = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Batch))), graphql_name='batches', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Batch_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Batch_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    solution = sgqlc.types.Field(Solution, graphql_name='solution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )
    solutions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Solution))), graphql_name='solutions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Solution_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Solution_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class Token(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'address', 'from_batch_id', 'symbol', 'decimals', 'name', 'create_epoch', 'tx_hash')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    from_batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='fromBatchId')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    decimals = sgqlc.types.Field(BigInt, graphql_name='decimals')
    name = sgqlc.types.Field(String, graphql_name='name')
    create_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createEpoch')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')


class Trade(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'order', 'owner', 'sell_volume', 'buy_volume', 'trade_batch_id', 'trade_epoch', 'buy_token', 'sell_token', 'create_epoch', 'revert_epoch', 'tx_hash', 'tx_log_index')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    order = sgqlc.types.Field(sgqlc.types.non_null(Order), graphql_name='order')
    owner = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='owner')
    sell_volume = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='sellVolume')
    buy_volume = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='buyVolume')
    trade_batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tradeBatchId')
    trade_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tradeEpoch')
    buy_token = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='buyToken')
    sell_token = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='sellToken')
    create_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createEpoch')
    revert_epoch = sgqlc.types.Field(BigInt, graphql_name='revertEpoch')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')
    tx_log_index = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='txLogIndex')


class User(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'from_batch_id', 'orders', 'deposits', 'withdraw_requests', 'withdrawals', 'create_epoch', 'tx_hash')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    from_batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='fromBatchId')
    orders = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Order))), graphql_name='orders', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Order_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Order_filter, graphql_name='where', default=None)),
))
    )
    deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Deposit))), graphql_name='deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Deposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Deposit_filter, graphql_name='where', default=None)),
))
    )
    withdraw_requests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WithdrawRequest'))), graphql_name='withdrawRequests', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(WithdrawRequest_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(WithdrawRequest_filter, graphql_name='where', default=None)),
))
    )
    withdrawals = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Withdraw'))), graphql_name='withdrawals', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Withdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Withdraw_filter, graphql_name='where', default=None)),
))
    )
    create_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createEpoch')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')


class Withdraw(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'user', 'token_address', 'amount', 'create_epoch', 'create_batch_id', 'tx_hash')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')
    token_address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='tokenAddress')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    create_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createEpoch')
    create_batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createBatchId')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')


class WithdrawRequest(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'user', 'token_address', 'amount', 'withdrawable_from_batch_id', 'create_epoch', 'create_batch_id', 'tx_hash')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')
    token_address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='tokenAddress')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    withdrawable_from_batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='withdrawableFromBatchId')
    create_epoch = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createEpoch')
    create_batch_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createBatchId')
    tx_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txHash')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
graphql_schema.query_type = Query
graphql_schema.mutation_type = None
graphql_schema.subscription_type = Subscription

