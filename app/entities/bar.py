"""Defines market bar entities and related enums for representing trading data.

Includes:
- FrameType, MarketType, VenueId, Provider, ImbalanceDir enums
- Bar Pydantic model for market bar data
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel


class FrameType(str, Enum):
    """Enum representing the type of frame for market bars."""

    bar = "bar"


class MarketType(str, Enum):
    """Enum representing the type of market: centralized or OTC."""

    centralized = "centralized"
    otc = "otc"


class VenueId(str, Enum):
    """Enum representing the venue IDs for market data."""

    B3 = "B3"
    ACTIVE_TRADES = "ACTIVE_TRADES"
    BINANCE = "BINANCE"
    # Adicione outros venues conforme necessário


class Provider(str, Enum):
    """Enum representing the data providers for market data."""

    binance_ws_kline = "binance-ws-kline"
    metatrader = "metatrader"
    tradeview = "tradeview"
    screen_ocr = "screen-ocr"
    # Adicione outros providers conforme necessário


class ImbalanceDir(str, Enum):
    """Enum representing the imbalance direction for market bars."""

    up = "up"
    down = "down"
    flat = "flat"


class Bar(BaseModel):
    """Modelo que representa um bar de mercado."""

    tf: str  # Timeframe como string (ex: "1m", "5m", "1h", etc.)
    frame_type: FrameType  # Tipo de frame, sempre "bar"
    tf_s: int  # Timeframe em segundos
    market_type: MarketType  # Tipo de mercado: "centralized" ou "otc"
    venue_id: VenueId  # Identificador do venue: "B3", "ACTIVE_TRADES", "BINANCE", etc.
    venue_symbol: str  # Símbolo como aparece no venue
    instrument_uid: str  # Identificador canônico do instrumento
    provider: Provider  # Origem dos dados: "binance-ws-kline", "metatrader", "screen-ocr", etc.
    window_start_ms: int  # Início da janela (UTC, alinhado ao TF)
    window_end_ms: int  # Fim da janela (= start + tf_s*1000 - 1)
    is_final: bool  # Indica se o bar está fechado/finalizado
    open: float  # Preço de abertura
    high: float  # Preço máximo
    low: float  # Preço mínimo
    close: float  # Preço de fechamento
    volume: float  # Volume negociado
    ts_emit_ms: int  # Timestamp de emissão/registro do bar
    quality: dict[str, Any] | None = None  # Qualidade do bar (ex: {"filled": true, "had_gap": false})
    imbalance_dir: ImbalanceDir | None = None  # Direção do imbalance: "up", "down" ou "flat" (opcional)
