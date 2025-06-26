import re
from typing import Dict, List, Tuple

try:
    from crewai import Agent
except ImportError:  # pragma: no cover - crewai is optional for testing
    Agent = None


def _score_patterns(text: str, patterns: List[Tuple[str, float]]) -> Tuple[float, List[str]]:
    """Calcula pontuação e registra correspondências de padrões."""
    score = 0.0
    matches = []
    for pattern, weight in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            score += weight
            matches.append(pattern)
    return score, matches


TIPO_PADROES = {
    "contrato": [
        (r"\bcl[\u00e1a]usula\b", 1.0),
        (r"pelo presente contrato", 1.0),
        (r"contratante", 0.5),
        (r"contratada", 0.5),
        (r"obrigaç[\u00e3a]o", 0.3),
        (r"valor", 0.2),
        (r"prestaç[\u00e3a]o de serviços", 0.7),
    ],
    "petição": [
        (r"excelent[\u00edi]ssim[oa]", 1.0),
        (r"vossa excelência", 0.8),
        (r"autor", 0.5),
        (r"r[\u00e9e]u", 0.5),
        (r"petiç[\u00e3a]o", 0.8),
        (r"tribunal", 0.5),
    ],
    "edital de licitação": [
        (r"objeto da licitaç[\u00e3a]o", 1.0),
        (r"lote", 0.5),
        (r"n[\u00ba\u00ba] do edital", 0.8),
        (r"licitante", 0.8),
        (r"proposta", 0.3),
        (r"preg[\u00e3a]o", 0.3),
    ],
    "parecer jurídico": [
        (r"parecer", 1.0),
        (r"jurisprud[\u00ea]ncia", 0.5),
        (r"opina", 0.5),
        (r"conclus[\u00e3a]o", 0.5),
    ],
    "recurso": [
        (r"recurso", 1.0),
        (r"apelaç[\u00e3a]o", 0.8),
        (r"agravo", 0.5),
        (r"contrarrazoes", 0.5),
    ],
    "procuração": [
        (r"outorgante", 0.8),
        (r"outorgado", 0.8),
        (r"poderes", 0.5),
        (r"procuraç[\u00e3a]o", 1.0),
    ],
    "termo aditivo": [
        (r"termo aditivo", 1.0),
        (r"aditivar", 0.8),
        (r"cl[\u00e1a]usula", 0.5),
        (r"alteraç[\u00e3a]o", 0.5),
    ],
}

SUBTIPO_PADROES = {
    "contrato": [
        ("contrato de prestação de serviços", r"prestaç[\u00e3a]o de serviços"),
        ("contrato de compra e venda", r"compra e venda"),
    ],
    "petição": [
        ("petição inicial", r"petiç[\u00e3a]o inicial"),
        ("contestação", r"contestaç[\u00e3a]o"),
    ],
    "edital de licitação": [
        ("pregão", r"preg[\u00e3a]o"),
        ("concorrência", r"concorrência"),
    ],
    "recurso": [
        ("apelação", r"apelaç[\u00e3a]o"),
        ("agravo", r"agravo"),
    ],
}


def _detectar_subtipo(tipo: str, text: str) -> str:
    for subtipo, pattern in SUBTIPO_PADROES.get(tipo, []):
        if re.search(pattern, text, flags=re.IGNORECASE):
            return subtipo
    return ""


def classificar_documento(texto_limpo: str) -> Dict[str, object]:
    if not texto_limpo:
        return {
            "tipo_documento": "desconhecido",
            "subtipo": "",
            "confiança": 0.0,
            "racional": "Texto vazio ou não informado",
        }

    texto = texto_limpo.lower()
    resultados = {}
    rastros = {}

    for tipo, patterns in TIPO_PADROES.items():
        score, matches = _score_patterns(texto, patterns)
        resultados[tipo] = score
        if matches:
            rastros[tipo] = matches

    tipo_escolhido = max(resultados, key=resultados.get)
    pontuacao_max = resultados[tipo_escolhido]
    soma_scores = sum(resultados.values())
    confianca = pontuacao_max / soma_scores if soma_scores else 0.0
    subtipo = _detectar_subtipo(tipo_escolhido, texto)
    racional = "; ".join(rastros.get(tipo_escolhido, []))

    return {
        "tipo_documento": tipo_escolhido if pontuacao_max > 0 else "desconhecido",
        "subtipo": subtipo,
        "confiança": round(confianca, 2),
        "racional": racional,
    }


if Agent is not None:
    ClassificadorJuridicoAgent = Agent(
        name="Classificador Jurídico",
        description="Identifica o tipo de documento jurídico com base no conteúdo textual.",
        function=classificar_documento,
        return_type=dict,
    )
