"""
Copyright 2019 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from gs_quant.base import *
from gs_quant.common import *
import datetime
from typing import Dict, Optional, Tuple, Union
from dataclasses import dataclass, field
from dataclasses_json import LetterCase, config, dataclass_json
from gs_quant.instrument.core import Instrument, resolution_safe


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class AssetRef(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    product_code: Optional[ProductCode] = field(default=None, metadata=field_metadata)
    size: Optional[float] = field(default=None, metadata=field_metadata)
    asset_id: Optional[str] = field(default=None, metadata=field_metadata)
    number_of_options: Optional[float] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Cross_Asset, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Any, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class Bond(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    identifier: Optional[str] = field(default=None, metadata=field_metadata)
    identifier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    size: Optional[float] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Cross_Asset, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Bond, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class Cash(Instrument):
    currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    payment_date: Optional[datetime.date] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Cash, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Cash, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CommodOTCOptionPeriod(Instrument):
    start: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    end: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    quantity: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Commod, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.OptionPeriod, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CommodOTCSwapLeg(Instrument):
    fixing_currency: Optional[CurrencyName] = field(default=None, metadata=field_metadata)
    leg_description: Optional[str] = field(default=None, metadata=field_metadata)
    contract: Optional[str] = field(default=None, metadata=field_metadata)
    fixing_currency_source: Optional[str] = field(default=None, metadata=field_metadata)
    underlier: Optional[str] = field(default=None, metadata=field_metadata)
    quantity_multiplier: Optional[int] = field(default=None, metadata=field_metadata)
    fixed_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Commod, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.SwapLeg, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CommodSwap(Instrument):
    commodity: Optional[str] = field(default=None, metadata=field_metadata)
    quantity: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    contract: Optional[str] = field(default=None, metadata=field_metadata)
    fixing_currency_source: Optional[str] = field(default=None, metadata=field_metadata)
    start: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_type: Optional[str] = field(default=None, metadata=field_metadata)
    number_of_periods: Optional[int] = field(default=None, metadata=field_metadata)
    quantity_unit: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement: Optional[str] = field(default=None, metadata=field_metadata)
    fixing_currency: Optional[CurrencyName] = field(default=None, metadata=field_metadata)
    fixed_price_unit: Optional[str] = field(default=None, metadata=field_metadata)
    commodity_reference_price: Optional[str] = field(default=None, metadata=field_metadata)
    end: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    quantity_period: Optional[Period] = field(default=None, metadata=field_metadata)
    strategy: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Commod, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Swap, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqAutoroll(Instrument):
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    first_fixing_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    last_fixing_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixing_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    trigger_level: Optional[float] = field(default=None, metadata=field_metadata)
    buffer_level: Optional[float] = field(default=None, metadata=field_metadata)
    local_return_cap: Optional[float] = field(default=None, metadata=field_metadata)
    upside_leverage: Optional[float] = field(default=None, metadata=field_metadata)
    initial_fixing_override: Optional[float] = field(default=None, metadata=field_metadata)
    apply_trigger_level_shift: Optional[str] = field(default=None, metadata=field_metadata)
    trigger_level_shift: Optional[float] = field(default=None, metadata=field_metadata)
    notional: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    business_day_calendar: Optional[str] = field(default=None, metadata=field_metadata)
    payment_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_delay: Optional[str] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    premium: Optional[float] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Autoroll, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqBinary(Instrument):
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    currency: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Binary, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqCliquet(Instrument):
    return_style: Optional[str] = field(default='Rate of Return', metadata=field_metadata)
    last_valuation_date: Optional[datetime.date] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    payment_frequency: Optional[str] = field(default='Maturity', metadata=field_metadata)
    global_cap: Optional[float] = field(default=1000000.0, metadata=field_metadata)
    first_valuation_date: Optional[datetime.date] = field(default=None, metadata=field_metadata)
    currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    global_floor: Optional[float] = field(default=-1000000.0, metadata=field_metadata)
    strike_price: Optional[float] = field(default=None, metadata=field_metadata)
    return_type: Optional[str] = field(default='Sum', metadata=field_metadata)
    valuation_period: Optional[str] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Cliquet, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqConvertibleBond(Instrument):
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    premium_settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    ref_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    quantity: Optional[float] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Convertible, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqForward(Instrument):
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    forward_price: Optional[float] = field(default=None, metadata=field_metadata)
    number_of_shares: Optional[int] = field(default=1, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Forward, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqFuture(Instrument):
    total_quantity: float = field(default=None, metadata=field_metadata)
    identifier: Optional[str] = field(default=None, metadata=field_metadata)
    identifier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    underlier: Optional[str] = field(default=None, metadata=field_metadata)
    multiplier: Optional[float] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    quantity: Optional[float] = field(default=None, metadata=field_metadata)
    currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    traded_price: Optional[float] = field(default=0.0, metadata=field_metadata)
    trade_as: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Future, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqOption(Instrument):
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    option_style: Optional[OptionStyle] = field(default=None, metadata=field_metadata)
    number_of_options: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    exchange: Optional[str] = field(default=None, metadata=field_metadata)
    multiplier: Optional[float] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium: Optional[float] = field(default=0.0, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    valuation_time: Optional[ValuationTime] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    trade_as: Optional[TradeAs] = field(default=None, metadata=field_metadata)
    future_contract: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Option, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)

    def scale_in_place(self, scaling: Optional[float] = None):
        if self.unresolved is None:
            raise RuntimeError('Can only scale resolved instruments')
        if scaling is None or scaling == 1:
            return
    
        if scaling < 0:
            flip_dict = {BuySell.Buy: BuySell.Sell, BuySell.Sell: BuySell.Buy}
            self.buy_sell = flip_dict[self.buy_sell]
            
        self.number_of_options *= abs(scaling)
        return


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqOptionLeg(Instrument):
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    option_style: Optional[OptionStyle] = field(default=None, metadata=field_metadata)
    multiplier: Optional[float] = field(default=None, metadata=field_metadata)
    number_of_options: Optional[float] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    valuation_time: Optional[ValuationTime] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium: Optional[float] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    trade_as: Optional[TradeAs] = field(default=None, metadata=field_metadata)
    exchange: Optional[str] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.OptionLeg, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqStock(Instrument):
    identifier: Optional[str] = field(default=None, metadata=field_metadata)
    identifier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    traded_price: Optional[float] = field(default=0.0, metadata=field_metadata)
    currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    quantity: Optional[float] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[datetime.date] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Single_Stock, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqSynthetic(Instrument):
    underlier: Union[float, str] = field(default=None, metadata=field_metadata)
    expiry: str = field(default=None, metadata=field_metadata)
    currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    swap_type: Optional[str] = field(default='Eq Swap', metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    effective_date: Optional[datetime.date] = field(default=None, metadata=field_metadata)
    num_of_underlyers: Optional[float] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Synthetic, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqVarianceSwap(Instrument):
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    variance_cap: Optional[float] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.VarianceSwap, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXBinary(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Binary, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXDoubleKnockout(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    knock_in_or_out: Optional[InOut] = field(default=None, metadata=field_metadata)
    lower_barrier_level: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    upper_barrier_level: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    knockout_convention: Optional[KnockoutConvention] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.DoubleKnockout, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXDoubleOneTouch(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    lower_barrier_level: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    upper_barrier_level: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    payout_type: Optional[PayoutType] = field(default=None, metadata=field_metadata)
    knockout_convention: Optional[KnockoutConvention] = field(default=None, metadata=field_metadata)
    touch_or_no_touch: Optional[TouchNoTouch] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.DoubleTouch, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXEuropeanKnockout(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[str] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    barrier_level: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    knock_up_or_down: Optional[UpDown] = field(default=None, metadata=field_metadata)
    knock_in_or_out: Optional[InOut] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.EuropeanKnockout, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXForward(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    forward_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount_in_other_currency: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Forward, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXKnockout(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    knock_in_or_out: Optional[InOut] = field(default=None, metadata=field_metadata)
    knock_up_or_down: Optional[UpDown] = field(default=None, metadata=field_metadata)
    barrier_level: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    knockout_convention: Optional[KnockoutConvention] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Knockout, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXMultiCrossBinaryLeg(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    fixing_source: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.MultiCrossBinaryLeg, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXOneTouch(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    knock_up_or_down: Optional[UpDown] = field(default=None, metadata=field_metadata)
    knockout_convention: Optional[KnockoutConvention] = field(default=None, metadata=field_metadata)
    touch_or_no_touch: Optional[TouchNoTouch] = field(default=None, metadata=field_metadata)
    payout_type: Optional[PayoutType] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.OneTouch, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXOption(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount_in_other_currency: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Option, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXOptionLeg(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount_in_other_currency: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.OptionLeg, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXShiftingBermForward(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount_in_other_currency: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    window_start_date: Optional[str] = field(default=None, metadata=field_metadata)
    exercise_decision_freq: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.ShiftingBermForward, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXTarfScheduleLeg(Instrument):
    profit_strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    loss_strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    fixing_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.TarfScheduleLeg, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXVolatilitySwap(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    strike_vol: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    first_fixing_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    last_fixing_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixing_source: Optional[str] = field(default=None, metadata=field_metadata)
    fixing_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    annualization_factor: Optional[float] = field(default=None, metadata=field_metadata)
    calculate_mean_return: Optional[float] = field(default=0.0, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.VolatilitySwap, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class Forward(Instrument):
    currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Cash, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Forward, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRBondFuture(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    exchange: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.BondFuture, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRCap(Instrument):
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    cap_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Cap, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRFloor(Instrument):
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    floor_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Floor, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class InflationSwap(Instrument):
    pay_or_receive: Optional[PayReceive] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    index: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fixed_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    base_cpi: Optional[float] = field(default=None, metadata=field_metadata)
    clearing_house: Optional[SwapClearingHouse] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.InflationSwap, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)

    def scale_in_place(self, scaling: Optional[float] = None):
        if self.unresolved is None:
            raise RuntimeError('Can only scale resolved instruments')
        if scaling is None or scaling == 1:
            return
    
        if scaling < 0:
            flip_dict = {PayReceive.Pay: PayReceive.Receive, PayReceive.Receive: PayReceive.Pay}
            self.pay_or_receive = flip_dict[self.pay_or_receive]
            self.fee *= -1
        self.notional_amount *= abs(scaling)
        return


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class InstrumentsRepoIRDiscreteLock(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    spot_clean_price: Optional[float] = field(default=None, metadata=field_metadata)
    settlement: Optional[str] = field(default=None, metadata=field_metadata)
    repo_rate: Optional[float] = field(default=None, metadata=field_metadata)
    forward_clean_price: Optional[float] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Repo, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Bond_Forward, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CDIndex(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    clearinghouse: Optional[SwapClearingHouse] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    first_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    first_roll_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    index_family: Optional[str] = field(default=None, metadata=field_metadata)
    index_for_basis: Optional[str] = field(default=None, metadata=field_metadata)
    index_series: Optional[float] = field(default=None, metadata=field_metadata)
    index_version: Optional[float] = field(default=None, metadata=field_metadata)
    isda_docs: Optional[str] = field(default='2014', metadata=config(field_name='ISDADocs', exclude=exclude_none))
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Credit, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Index, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CDIndexOption(Instrument):
    automatic_exercise: Optional[float] = field(default=0.0, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    clearinghouse: Optional[SwapClearingHouse] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    earliest_exercise_time: Optional[str] = field(default=None, metadata=field_metadata)
    earliest_exercise_time_centre: Optional[str] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    exercise_date_business_day_convention: Optional[BusinessDayConvention] = field(default='Following', metadata=field_metadata)
    exercise_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    expiration_time_centre: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[float] = field(default=0.0, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    first_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    first_roll_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    index_family: Optional[str] = field(default=None, metadata=field_metadata)
    index_for_basis: Optional[str] = field(default=None, metadata=field_metadata)
    index_series: Optional[float] = field(default=None, metadata=field_metadata)
    index_version: Optional[float] = field(default=None, metadata=field_metadata)
    isda_docs: Optional[str] = field(default='2014', metadata=config(field_name='ISDADocs', exclude=exclude_none))
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    fixed_rate: Optional[float] = field(default=None, metadata=field_metadata)
    strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    strike_type: Optional[str] = field(default='Spread', metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Credit, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.IndexOption, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CommodOTCOptionLeg(Instrument):
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    fixing_currency: Optional[CurrencyName] = field(default=None, metadata=field_metadata)
    premium: Optional[CommodPrice] = field(default=None, metadata=field_metadata)
    leg_description: Optional[str] = field(default=None, metadata=field_metadata)
    contract: Optional[str] = field(default=None, metadata=field_metadata)
    fixing_currency_source: Optional[str] = field(default=None, metadata=field_metadata)
    strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    underlier: Optional[str] = field(default=None, metadata=field_metadata)
    premium_settlement: Optional[str] = field(default=None, metadata=field_metadata)
    quantity_multiplier: Optional[int] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Commod, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.OptionLeg, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CommodOTCSwap(Instrument):
    quantity: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    legs: Optional[Tuple[CommodOTCSwapLeg, ...]] = field(default=None, metadata=field_metadata)
    start: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    end: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    number_of_periods: Optional[int] = field(default=None, metadata=field_metadata)
    quantity_unit: Optional[str] = field(default=None, metadata=field_metadata)
    quantity_period: Optional[Period] = field(default=None, metadata=field_metadata)
    strategy: Optional[str] = field(default=None, metadata=field_metadata)
    settlement: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Commod, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.SwapStrategy, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CommodOption(Instrument):
    commodity: Optional[str] = field(default=None, metadata=field_metadata)
    number_of_periods: Optional[int] = field(default=None, metadata=field_metadata)
    quantity_unit: Optional[str] = field(default=None, metadata=field_metadata)
    currency_summary: Optional[CurrencyName] = field(default=None, metadata=field_metadata)
    option_types: Optional[Tuple[str, ...]] = field(default=None, metadata=field_metadata)
    settlement: Optional[str] = field(default=None, metadata=field_metadata)
    option_type: Optional[str] = field(default=None, metadata=field_metadata)
    strike_unit: Optional[str] = field(default=None, metadata=field_metadata)
    strikes: Optional[Tuple[str, ...]] = field(default=None, metadata=field_metadata)
    end: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    buy_sells: Optional[Tuple[str, ...]] = field(default=None, metadata=field_metadata)
    underlier_short_name: Optional[str] = field(default=None, metadata=field_metadata)
    settlement_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    strike_currency: Optional[CurrencyName] = field(default=None, metadata=field_metadata)
    quantity: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    contract: Optional[str] = field(default=None, metadata=field_metadata)
    fixing_currency_source: Optional[str] = field(default=None, metadata=field_metadata)
    strike: Optional[str] = field(default=None, metadata=field_metadata)
    start: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_type: Optional[str] = field(default=None, metadata=field_metadata)
    fixing_currency: Optional[CurrencyName] = field(default=None, metadata=field_metadata)
    commodity_reference_price: Optional[str] = field(default=None, metadata=field_metadata)
    quantity_period: Optional[str] = field(default=None, metadata=field_metadata)
    strategy: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[str] = field(default=None, metadata=field_metadata)
    period_details: Optional[Tuple[CommodOTCOptionPeriod, ...]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Commod, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Option, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CommodVolVarSwap(Instrument):
    notional_currency: Optional[CurrencyName] = field(default=None, metadata=field_metadata)
    notional: Optional[float] = field(default=1.0, metadata=field_metadata)
    floating_rate_is_capped: Optional[str] = field(default=None, metadata=field_metadata)
    end_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    margined: Optional[float] = field(default=None, metadata=field_metadata)
    market_disruption_agreement: Optional[str] = field(default=None, metadata=field_metadata)
    mean_rule: Optional[CommodMeanRule] = field(default=None, metadata=field_metadata)
    divisor: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_mean: Optional[float] = field(default=None, metadata=field_metadata)
    first_fixing: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    floating_rate_cap: Optional[float] = field(default=None, metadata=field_metadata)
    fx_fixing_source: Optional[str] = field(default=None, metadata=field_metadata)
    annualization_factor: Optional[float] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    contract: Optional[str] = field(default=None, metadata=field_metadata)
    strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    swap_type: Optional[str] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixing_currency: Optional[CurrencyName] = field(default=None, metadata=field_metadata)
    asset_fixing_source: Optional[str] = field(default=None, metadata=field_metadata)
    sampling_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    variance_convention: Optional[VarianceConvention] = field(default=None, metadata=field_metadata)
    extra_sampling_calendars: Optional[str] = field(default='--Blank--', metadata=field_metadata)
    asset: Optional[str] = field(default=None, metadata=field_metadata)
    start_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Commod, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.VolVarSwap, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class EqOptionStrategy(Instrument):
    underlier: Union[float, str] = field(default=None, metadata=field_metadata)
    strategy: str = field(default=None, metadata=field_metadata)
    legs: Tuple[EqOptionLeg, ...] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    option_style: Optional[OptionStyle] = field(default=None, metadata=field_metadata)
    number_of_options: Optional[float] = field(default=None, metadata=field_metadata)
    multiplier: Optional[float] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium: Optional[float] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    valuation_time: Optional[ValuationTime] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    exchange: Optional[str] = field(default=None, metadata=field_metadata)
    trade_as: Optional[TradeAs] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Equity, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.OptionStrategy, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FRA(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    clearing_house: Optional[SwapClearingHouse] = field(default=None, metadata=field_metadata)
    clearing_legally_binding: Optional[float] = field(default=None, metadata=field_metadata)
    day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    frequency: Optional[str] = field(default=None, metadata=field_metadata)
    calendar: Optional[str] = field(default=None, metadata=field_metadata)
    rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    maturity: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    payment_delay: Optional[str] = field(default=None, metadata=field_metadata)
    roll_convention: Optional[str] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.FRA, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXMultiCrossBinary(Instrument):
    legs: Tuple[FXMultiCrossBinaryLeg, ...] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.MultiCrossBinary, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXOptionStrategy(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    strategy_name: Optional[str] = field(default=None, metadata=field_metadata)
    legs: Optional[Tuple[FXOptionLeg, ...]] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount_in_other_currency: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    strike_price: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    expiration_time: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.OptionStrategy, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class FXTarf(Instrument):
    pair: Optional[str] = field(default=None, metadata=field_metadata)
    new_or_unwind: Optional[NewOrUnwind] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    profit_strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    loss_strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fixing_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    method_of_settlement: Optional[OptionSettlementMethod] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[str] = field(default=None, metadata=field_metadata)
    long_or_short: Optional[LongShort] = field(default=None, metadata=field_metadata)
    european_knock_in: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    number_of_expiry: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    coupon_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    first_fixing_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    leverage_ratio: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    target_type: Optional[TargetType] = field(default=None, metadata=field_metadata)
    target: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    schedules: Optional[Tuple[FXTarfScheduleLeg, ...]] = field(default=None, metadata=field_metadata)
    target_adj_notional_or_strike: Optional[NotionalOrStrike] = field(default=None, metadata=field_metadata)
    payment_on_hitting_target: Optional[TargetPaymentType] = field(default=None, metadata=field_metadata)
    settlement_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.FX, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Tarf, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRAssetSwapFxdFlt(Instrument):
    asw_type: Optional[AswType] = field(default=None, metadata=field_metadata)
    clearing_house: Optional[SwapClearingHouse] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=None, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    fixed_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fixed_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    floating_rate_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    floating_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    floating_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_fx: Optional[float] = field(default=None, metadata=field_metadata)
    floating_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    floating_maturity: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    identifier: Optional[str] = field(default=None, metadata=field_metadata)
    identifier_type: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    pay_or_receive: Optional[PayReceive] = field(default=None, metadata=field_metadata)
    roll_convention: Optional[str] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    floating_rate_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    traded_clean_price: Optional[float] = field(default=100.0, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.AssetSwapFxdFlt, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRAssetSwapFxdFxd(Instrument):
    asw_type: Optional[AswType] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=None, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    fixed_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fixed_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    coupon: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    asset_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    asset_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    asset_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    asset_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    identifier: Optional[str] = field(default=None, metadata=field_metadata)
    identifier_type: Optional[str] = field(default=None, metadata=field_metadata)
    asset_maturity: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_maturity: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    roll_convention: Optional[str] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    fixed_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    clean_price: Optional[float] = field(default=100.0, metadata=field_metadata)
    settlement_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.AssetSwapFxdFxd, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRBasisSwap(Instrument):
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    principal_exchange: Optional[PrincipalExchange] = field(default=None, metadata=field_metadata)
    payer_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    payer_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    payer_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    payer_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    payer_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    payer_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    receiver_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    receiver_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    receiver_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    clearing_house: Optional[SwapClearingHouse] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.BasisSwap, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRBondOption(Instrument):
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    option_type: Optional[OptionType] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    strike_type: Optional[BondStrikeType] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    settlement: Optional[SettlementType] = field(default=None, metadata=field_metadata)
    underlier_type: Optional[UnderlierType] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.BondOption, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRCMSOption(Instrument):
    cap_floor: Optional[str] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    index: Optional[str] = field(default=None, metadata=field_metadata)
    rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    multiplier: Optional[float] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.CMSOption, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRCMSOptionStrip(Instrument):
    cap_floor: Optional[str] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    index: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    reset_delay: Optional[str] = field(default=None, metadata=field_metadata)
    multiplier: Optional[float] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.CMSOptionStrip, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRCMSSpreadOption(Instrument):
    cap_floor: Optional[str] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    index1_tenor: Optional[str] = field(default=None, metadata=field_metadata)
    index2_tenor: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.CMSSpreadOption, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRCMSSpreadOptionStrip(Instrument):
    cap_floor: Optional[str] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    index1: Optional[str] = field(default=None, metadata=field_metadata)
    index2: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    reset_delay: Optional[str] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.CMSSpreadOptionStrip, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRFixedLeg(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    fixed_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    fixed_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fixed_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    principal_exchange: Optional[PrincipalExchange] = field(default=None, metadata=field_metadata)
    roll_convention: Optional[str] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.FixedLeg, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRFloatLeg(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    floating_rate_for_the_initial_calculation_period: Optional[float] = field(default=None, metadata=field_metadata)
    floating_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    floating_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    floating_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    floating_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    floating_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    principal_exchange: Optional[PrincipalExchange] = field(default=None, metadata=field_metadata)
    roll_convention: Optional[str] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    floating_rate_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.FloatLeg, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRSwap(Instrument):
    pay_or_receive: Optional[PayReceive] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    principal_exchange: Optional[PrincipalExchange] = field(default=None, metadata=field_metadata)
    floating_rate_for_the_initial_calculation_period: Optional[float] = field(default=None, metadata=field_metadata)
    floating_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    floating_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fixed_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    fixed_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    clearing_house: Optional[SwapClearingHouse] = field(default=None, metadata=field_metadata)
    fixed_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    floating_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    roll_convention: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Swap, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)

    def scale_in_place(self, scaling: Optional[float] = None):
        if self.unresolved is None:
            raise RuntimeError('Can only scale resolved instruments')
        if scaling is None or scaling == 1:
            return
    
        if scaling < 0:
            flip_dict = {PayReceive.Pay: PayReceive.Receive, PayReceive.Receive: PayReceive.Pay}
            self.pay_or_receive = flip_dict[self.pay_or_receive]
            self.fee *= -1
        self.notional_amount *= abs(scaling)
        return


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRSwaption(Instrument):
    pay_or_receive: Optional[PayReceive] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    expiration_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_spread: Optional[float] = field(default=None, metadata=field_metadata)
    floating_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fixed_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    fixed_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    strike: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    premium_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    clearing_house: Optional[SwapClearingHouse] = field(default=None, metadata=field_metadata)
    settlement: Optional[SwapSettlement] = field(default=None, metadata=field_metadata)
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.Swaption, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRXccySwap(Instrument):
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[float] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    principal_exchange: Optional[PrincipalExchange] = field(default=None, metadata=field_metadata)
    payer_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    payer_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    payer_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    payer_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    payer_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    payer_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    payer_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    receiver_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    receiver_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    receiver_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    receiver_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    initial_fx_rate: Optional[float] = field(default=None, metadata=field_metadata)
    payer_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    receiver_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    payer_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    receiver_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    payer_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    notional_reset_side: Optional[PayReceive] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.XccySwapMTM, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRXccySwapFixFix(Instrument):
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[float] = field(default=None, metadata=field_metadata)
    receiver_notional_amount: Optional[float] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    principal_exchange: Optional[PrincipalExchange] = field(default=None, metadata=field_metadata)
    payer_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    payer_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    payer_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    payer_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    payer_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    receiver_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    receiver_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    receiver_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    receiver_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.XccySwapFixFix, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRXccySwapFixFlt(Instrument):
    pay_or_receive: Optional[PayReceive] = field(default=None, metadata=field_metadata)
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    principal_exchange: Optional[PrincipalExchange] = field(default=None, metadata=field_metadata)
    floating_rate_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    floating_rate_for_the_initial_calculation_period: Optional[float] = field(default=None, metadata=field_metadata)
    floating_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    floating_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    floating_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    floating_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fixed_rate_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fixed_rate: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    fixed_rate_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    fixed_rate_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    fixed_rate_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    floating_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    fixed_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    floating_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.XccySwapFixFlt, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class IRXccySwapFltFlt(Instrument):
    termination_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    effective_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    principal_exchange: Optional[PrincipalExchange] = field(default=None, metadata=field_metadata)
    payer_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    payer_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    payer_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    payer_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    payer_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    payer_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    payer_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    receiver_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    receiver_spread: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    receiver_rate_option: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_designated_maturity: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_frequency: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_day_count_fraction: Optional[DayCountFraction] = field(default=None, metadata=field_metadata)
    receiver_business_day_convention: Optional[BusinessDayConvention] = field(default=None, metadata=field_metadata)
    fee: Optional[float] = field(default=0.0, metadata=field_metadata)
    fee_currency: Optional[Currency] = field(default=None, metadata=field_metadata)
    fee_payment_date: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    payer_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    receiver_first_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    payer_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    receiver_last_stub: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    payer_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    receiver_holidays: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.XccySwap, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CommodOTCOption(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    quantity: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    start: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    number_of_periods: Optional[int] = field(default=None, metadata=field_metadata)
    quantity_unit: Optional[str] = field(default=None, metadata=field_metadata)
    settlement: Optional[str] = field(default=None, metadata=field_metadata)
    premium_summary: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    legs: Optional[Tuple[CommodOTCOptionLeg, ...]] = field(default=None, metadata=field_metadata)
    end: Optional[Union[datetime.date, str]] = field(default=None, metadata=field_metadata)
    quantity_period: Optional[Period] = field(default=None, metadata=field_metadata)
    strategy: Optional[str] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Commod, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.OptionStrategy, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class InvoiceSpread(Instrument):
    buy_sell: Optional[BuySell] = field(default=None, metadata=field_metadata)
    notional_amount: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    underlier: Optional[Union[float, str]] = field(default=None, metadata=field_metadata)
    swap: Optional[IRSwap] = field(default=None, metadata=field_metadata)
    future: Optional[IRBondFuture] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Rates, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.InvoiceSpread, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@resolution_safe
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class CSLPython(Instrument):
    class_name: Optional[str] = field(default=None, metadata=field_metadata)
    denominated: Optional[Currency] = field(default=None, metadata=field_metadata)
    double_params: Optional[Tuple[CSLDouble, ...]] = field(default=None, metadata=field_metadata)
    date_params: Optional[Tuple[CSLDate, ...]] = field(default=None, metadata=field_metadata)
    string_params: Optional[Tuple[CSLString, ...]] = field(default=None, metadata=field_metadata)
    simple_schedule_params: Optional[Tuple[CSLSimpleSchedule, ...]] = field(default=None, metadata=field_metadata)
    schedule_params: Optional[Tuple[CSLSchedule, ...]] = field(default=None, metadata=field_metadata)
    currency_params: Optional[Tuple[CSLCurrency, ...]] = field(default=None, metadata=field_metadata)
    stock_params: Optional[Tuple[CSLStock, ...]] = field(default=None, metadata=field_metadata)
    index_params: Optional[Tuple[CSLIndex, ...]] = field(default=None, metadata=field_metadata)
    fx_cross_params: Optional[Tuple[CSLFXCross, ...]] = field(default=None, metadata=field_metadata)
    double_array_params: Optional[Tuple[CSLDoubleArray, ...]] = field(default=None, metadata=field_metadata)
    date_array_params: Optional[Tuple[CSLDateArray, ...]] = field(default=None, metadata=field_metadata)
    string_array_params: Optional[Tuple[CSLStringArray, ...]] = field(default=None, metadata=field_metadata)
    simple_schedule_array_params: Optional[Tuple[CSLSimpleScheduleArray, ...]] = field(default=None, metadata=field_metadata)
    schedule_array_params: Optional[Tuple[CSLScheduleArray, ...]] = field(default=None, metadata=field_metadata)
    currency_array_params: Optional[Tuple[CSLCurrencyArray, ...]] = field(default=None, metadata=field_metadata)
    stock_array_params: Optional[Tuple[CSLStockArray, ...]] = field(default=None, metadata=field_metadata)
    index_array_params: Optional[Tuple[CSLIndexArray, ...]] = field(default=None, metadata=field_metadata)
    fx_cross_array_params: Optional[Tuple[CSLFXCrossArray, ...]] = field(default=None, metadata=field_metadata)
    asset_class: Optional[AssetClass] = field(init=False, default=AssetClass.Cross_Asset, metadata=field_metadata)
    type_: Optional[AssetType] = field(init=False, default=AssetType.CSL, metadata=config(field_name='type', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)
