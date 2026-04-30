# tests/test_app.py - Demo Testlər

import pytest
from app import toplayin, vurun, faktorial


class TestToplayin:
    def test_musbət_ədədlər(self):
        assert toplayin(2, 3) == 5

    def test_mənfi_ədədlər(self):
        assert toplayin(-1, -2) == -3

    def test_sıfır(self):
        assert toplayin(0, 5) == 5


class TestVurun:
    def test_sadə_vurma(self):
        assert vurun(3, 4) == 12

    def test_sıfırla_vurma(self):
        assert vurun(0, 99) == 0

    def test_mənfi_vurma(self):
        assert vurun(-2, 5) == -10


class TestFaktorial:
    def test_sıfır(self):
        assert faktorial(0) == 1

    def test_bir(self):
        assert faktorial(1) == 1

    def test_beş(self):
        assert faktorial(5) == 120

    def test_mənfi_xəta(self):
        with pytest.raises(ValueError):
            faktorial(-1)
