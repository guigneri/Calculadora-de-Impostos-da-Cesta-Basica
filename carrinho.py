"""
Semana 2 — O carrinho de compras (Orientação a Objetos: composição)

Complete os trechos marcados com TODO.
Não altere os nomes da classe e dos métodos: a correção é automática.
"""

from produtos import ALIQUOTA_PADRAO, Produto


class Carrinho:
    """Guarda produtos e suas quantidades."""

    def __init__(self):
        # Sugestão: um dicionário  nome -> [produto, quantidade]
        self._itens = {}

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        if not isinstance(produto, Produto):
            raise TypeError("Só é possível adicionar instâncias de Produto.")
       
        if (not isinstance(quantidade, int) or isinstance(quantidade, bool)
                or quantidade < 1):
            raise ValueError("A quantidade deve ser um inteiro maior ou igual a 1.")

        if produto.nome in self._itens:
            self._itens[produto.nome][1] += quantidade
        else:
            self._itens[produto.nome] = [produto, quantidade]

    def remover(self, nome: str) -> None:
       if nome not in self._itens:
            raise KeyError(f"Produto '{nome}' não está no carrinho.")
       del self._itens[nome]

    def subtotal(self) -> float:
        """Soma de preco * quantidade (sem impostos)."""
        return round(sum(p.preco * q for p, q in self._itens.values()), 2)

    def total_impostos(self) -> float:
        """Soma de produto.imposto() * quantidade."""
        return round(sum(p.imposto() * q for p, q in self._itens.values()), 2)

    def total(self) -> float:
        """subtotal() + total_impostos()"""
        return round(self.subtotal() + self.total_impostos(), 2)

    def economia(self) -> float:
        """
        Quanto o consumidor pagaria A MAIS se todos os produtos
        tivessem a alíquota padrão:
            soma de round(preco * ALIQUOTA_PADRAO, 2) * quantidade
            menos total_impostos()
        """
        imposto_cheio = sum(
            round(p.preco * ALIQUOTA_PADRAO, 2) * q
            for p, q in self._itens.values()
        )
        return round(imposto_cheio - self.total_impostos(), 2)

    def __len__(self) -> int:
        """Total de UNIDADES no carrinho."""
        return sum(q for _, q in self._itens.values())

    def __contains__(self, nome: str) -> bool:
        """Permite: 'Arroz 5kg' in carrinho"""
        return nome in self._itens


if __name__ == "__main__":
    from produtos import ProdutoCestaBasica, ProdutoPadrao

    c = Carrinho()
    c.adicionar(ProdutoCestaBasica("Feijão 1kg", 8.00), 2)
    c.adicionar(ProdutoPadrao("Chocolate", 10.00))
    print(c.total_impostos())  # 2.5
    print(c.economia())        # 4.0
    print(len(c))          
